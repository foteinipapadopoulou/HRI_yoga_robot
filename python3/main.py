import stk.python27bridge
import stk.events
import stk.services
import time
import logging

MAX_TIME_POSE = 5

class NaoYogaInstructor:
	def __init__(self):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		
		self.running = False
		self.stop_flag = False
		self.poses = ["Posture1", "Posture2", "Posture3"] # [String]

		# Wake up robot
		self.s.ALMotion.wakeUp()
		self.s.ALRobotPosture.goToPosture("StandInit", 0.5)

		# Track face
		targetName = "Face"
		faceWidth = 0.1
		self.s.ALTracker.registerTarget(targetName, faceWidth)
		self.s.ALTracker.track(targetName)
		self.s.ALTracker.setMode("Head")

		# Photo capture
		self.s.ALPhotoCapture.setResolution(2)
		self.s.ALPhotoCapture.setPictureFormat("jpg")

		self.s.ALTextToSpeech.say("Hello, world!")

	def start(self, feedback=False):
		self.stop() # Stop any possible running session

		self.running = True
		self.stop_flag = False

		if feedback:
			self._yoga_with_feedback()
		else:
			self._yoga_without_feedback()

		if not self.stop_flag:
			self.s.ALTextToSpeech.say("Session completed!")

		self.running = False

	def stop(self):
		if self.running:
			self.stop_flag = True
			self.s.ALTextToSpeech.say("Received stop command.")
			while self.running:
				time.sleep(0.1)

	def _yoga_without_feedback(self):
		self.s.ALTextToSpeech.say("Let's start the yoga session!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			self._perform_pose(pose)
			time.sleep(MAX_TIME_POSE)

	def _yoga_with_feedback(self):
		self.s.ALTextToSpeech.say("Let's start the yoga session with feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			self._perform_pose(pose)
			self._feedback_loop(pose)

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
			time.sleep(1) # Remove this once self._analyse_pose() and self._give_feedback() are implemented
		
	def _capture_pose_image(self, pose):
		file_path_array = self.s.ALPhotoCapture.takePicture("/home/nao/recordings/cameras/", pose, overwrite=True)
		if file_path_array is None or not file_path_array:
			logging.error("Failed to capture image.")
			return None
		return file_path_array[0]

	def _analyze_pose(self, pose, image_file_path):
		pass

	def _give_feedback(self, analysis):
		pass

if __name__ == "__main__":
	naoYogaInstructor = NaoYogaInstructor()
	try:
		naoYogaInstructor.start(feedback=True)
	except KeyboardInterrupt:
		print("Interrupted by user")
		naoYogaInstructor.stop()
		print("Stopped")
