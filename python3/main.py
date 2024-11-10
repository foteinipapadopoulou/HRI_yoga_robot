import stk.python27bridge
import stk.events
import stk.services
import time

MAX_TIME_POSE = 5
INTEVAL_TIME_PHOTO = 1
IMAGE_SAVE_PATH = "/home/nao/recordings/cameras/"

class NaoYogaInstructor:
	def __init__(self, poses):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		
		self.poses = poses if poses is not None else ["Posture1", "Posture2", "Posture3"]
		self.running = False
		self.stop_flag = False

	def __enter__(self):
		# Wake up Nao
		self.s.ALMotion.wakeUp()
		self.s.ALRobotPosture.goToPosture("StandInit", 0.5)

		# Photo capture
		self.s.ALPhotoCapture.setResolution(2)
		self.s.ALPhotoCapture.setPictureFormat("jpg")

		# Face tracker
		target_name = "Face"
		face_width = 0.1
		self.s.ALTracker.registerTarget(target_name, face_width)
		self.s.ALTracker.setMode("Head")
		self.s.ALTracker.track(target_name)
		
		print("NaoYogaInstructor initialized!")
		self.s.ALTextToSpeech.say("Hello, world!")
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		print("Shutting down NaoYogaInstructor...")
		self._stop()

		try:
			self.s.ALTracker.stopTracker()
			self.s.ALTracker.unregisterAllTargets()
			print("Stopped tracker.")
		except Exception as e:
			print(f"Error stopping tracker: {e}")

		try:
			self.s.ALRobotPosture.goToPosture("Sit", 0.5)
			self.s.ALRobotPosture.rest()
			print("Nao is resting.")
		except Exception as e:
			print(f"Error setting Nao to rest: {e}")

		try:
			self.s.ALTextToSpeech.say("Goodbye. Shutting down now.")
		except Exception as e:
			print(f"Error with TextToSpeech: {e}")

		print("NaoYogaInstructor shutdown complete.")

	def start(self, feedback=False):
		self._stop() # Stop any possible running session

		try:
			if feedback:
				self._yoga_with_feedback()
			else:
				self._yoga_without_feedback()

			if not self.stop_flag:
				self.s.ALTextToSpeech.say("Session completed!")
		finally:
			self.running = False

	def _stop(self):
		if self.running:
			self.stop_flag = True
			while self.running:
				time.sleep(0.1)

	def _yoga_without_feedback(self):
		print("Starting yoga session without feedback.")
		self.s.ALTextToSpeech.say("Let's start the yoga session without feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			print(f"Performing pose: {pose}")
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			self._perform_pose(pose)
			time.sleep(MAX_TIME_POSE)
		print("Ended yoga session without feedback.")

	def _yoga_with_feedback(self):
		print("Starting yoga session with feedback.")
		self.s.ALTextToSpeech.say("Let's start the yoga session with feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			print(f"Performing pose: {pose}")
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			self._perform_pose(pose)
			self._feedback_loop(pose)
		print("Ended yoga session with feedback.")

	def _perform_pose(self, pose):
		pass

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
			file_path_array = self.s.ALPhotoCapture.takePicture(IMAGE_SAVE_PATH, pose, overwrite=True)
			if file_path_array is None or not file_path_array:
				print(f"Failed to capture image for {pose}: file_path_array is None or an empty array.")
				return None
			return file_path_array[0]
		except Exception as e:
			print(f"Error capturing image for {pose}: {e}")
			return None

	def _analyze_pose(self, pose, image_file_path):
		pass

	def _give_feedback(self, analysis):
		pass

if __name__ == "__main__":
	with NaoYogaInstructor(poses=None) as naoYogaInstructor:
		try:
			naoYogaInstructor.start(feedback=True)
		except KeyboardInterrupt:
			print("Interrupted by user!")
