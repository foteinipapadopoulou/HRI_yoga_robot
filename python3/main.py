import stk.python27bridge
import stk.events
import stk.services
import time
import logging

from constants import *
from utils import *


class NaoYogaInstructor:
	def __init__(self, poses):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		self.speechProxy = self.s.ALTextToSpeech
		self.motionProxy = self.s.ALMotion
		self.postureProxy = self.s.ALRobotPosture
		self.photoCaptureProxy = self.s.ALPhotoCapture
		self.activityLifeProxy = self.s.ALAutonomousLife
		self.trackerProxy = self.s.ALTracker

		logging.basicConfig(level=logging.INFO) # using of logging module to log messages on Choreographe console
		self.logger = logging.getLogger(__name__)

		self.activityLifeProxy.setState("disabled") # we need to disable autonomous life to control the robot's movements
		
		self.poses = poses if poses is not None else ["warrior", "chair"] 
		self.running = False
		self.stop_flag = False

	def __enter__(self):
		# Wake up Nao
		self.motionProxy.wakeUp()
		self.postureProxy.goToPosture("StandInit", 0.5)
		time.sleep(MAX_TIME_POSE)
		# Photo capture
		self.photoCaptureProxy.setResolution(2)
		self.photoCaptureProxy.setPictureFormat("jpg")

		# Face tracker
		target_name = "Face"
		face_width = 0.1
		self.trackerProxy.registerTarget(target_name, face_width)
		self.trackerProxy.setMode("Head")
		self.trackerProxy.track(target_name)
		
		self.logger.info("NaoYogaInstructor initialized!")
		self.speechProxy.say("Hello, world!")
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.logger.info("Shutting down NaoYogaInstructor...")
		self._stop()

		try:
			self.trackerProxy.stopTracker()
			self.trackerProxy.unregisterAllTargets()
			self.logger.info("Stopped tracker.")
		except Exception as e:
			self.logger.error(f"Error stopping tracker: {e}")

		try:
			self.postureProxy.goToPosture("Sit", 0.5)
			self.postureProxy.rest()
			self.logger.info("Nao is resting.")
		except Exception as e:
			self.logger.error(f"Error setting Nao to rest: {e}")

		try:
			self.speechProxy.say("Goodbye. Shutting down now.")
		except Exception as e:
			self.logger.error(f"Error with TextToSpeech: {e}")

		self.logger.info("NaoYogaInstructor shutdown complete.")

		# self.speechProxy.say("Hello, world")

	def start(self, feedback=False):
		self._stop() # Stop any possible running session

		try:
			if feedback:
				self._yoga_with_feedback()
			else:
				self._yoga_without_feedback()

			if not self.stop_flag:
				self.speechProxy.say("Session completed!")
		finally:
			self.running = False

	def _stop(self):
		if self.running:
			self.stop_flag = True
			while self.running:
				time.sleep(0.1)

	def _yoga_without_feedback(self):
		self.logger.info("Starting yoga session without feedback.")
		self.speechProxy.say("Let's start the yoga session without feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.logger.info(f"Performing pose: {pose}")
			self.speechProxy.say(f"Now, {pose} pose.")
			self._perform_pose(pose)

		self.logger.info("Ended yoga session without feedback.")

	def _yoga_with_feedback(self):
		self.logger.info("Starting yoga session with feedback.")
		self.speechProxy.say("Let's start the yoga session with feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.logger.info(f"Performing pose: {pose}")
			self.speechProxy.say(f"Now, {pose} pose.")
			self._perform_pose(pose)
			self._feedback_loop(pose)
		self.logger.info("Ended yoga session with feedback.")

	def _perform_pose(self, pose):
		# set initial posture
		initial_posture = get_initial_posture_for_pose(pose)
		self.logger.info(f"Setting initial posture: {initial_posture}")
		self.postureProxy.goToPosture("StandInit", 0.5)
		time.sleep(MAX_TIME_POSE)

		# get angles for pose
		self.logger.info(f"Getting angles for pose: {pose}")
		angles = get_angles_for_pose(pose)
		self.logger.info(f"Angles for pose: {angles}")

		# start nao saying instructions for pose
		instructions = get_instructions_for_pose(pose)
		self.logger.info(f"Nao will say the instructions for pose: {pose}")
		self.speechProxy.say(instructions)
		time.sleep(MAX_TIME_POSE)
		
		# set stiffness off and move nao to pose
		self.logger.info(f"Set stiffness on for all joints.")
		self._stiffness_on()
		self.logger.info(f"Moving to pose: {pose}")
		for key, value in angles.items():
			self.motionProxy.setAngles(key, value, SPEED_POSE)
		time.sleep(MAX_TIME_POSE)

	def _stiffness_on(self):
		# We use the "Body" name to signify the collection of all joints
		pNames = "Body"
		pStiffnessLists = 1.0
		pTimeLists = 1.0
		self.motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

	def _feedback_loop(self, pose):
		start_time = time.time()
		while True:
			if self.stop_flag:
				break
			elapsed_time = time.time() - start_time
			if elapsed_time > MAX_TIME_POSE:
				break
			image_file_path = self._capture_pose_image(pose)
			analysis = self._analyze_pose(pose, image_file_path)
			self._give_feedback(analysis)
			time.sleep(INTEVAL_TIME_PHOTO)
		
	def _capture_pose_image(self, pose):
		try:
			file_path_array = self.photoCaptureProxy.takePicture(IMAGE_SAVE_PATH, pose, overwrite=True)
			if file_path_array is None or not file_path_array:
				self.logger.info(f"Failed to capture image for {pose}: file_path_array is None or an empty array.")
				return None
			return file_path_array[0]
		except Exception as e:
			self.logger.error(f"Error capturing image for {pose}: {e}")
			return None

	def _analyze_pose(self, pose, image_file_path):
		pass

	def _give_feedback(self, analysis):
		pass

if __name__ == "__main__":
	with NaoYogaInstructor(poses=None) as naoYogaInstructor:
		try:
			naoYogaInstructor.start(feedback=False)
		except KeyboardInterrupt:
			naoYogaInstructor.logger.error("Interrupted by user!")
