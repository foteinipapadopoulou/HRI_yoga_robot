import stk.python27bridge
import stk.events
import stk.services
import time

class NaoYogaInstructor:
	def __init__(self):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		
		self.running = False
		self.stop_flag = False
		self.poses = [] # [String]

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
			self.s.ALTextToSpeech.say("Bye, world!")

	def _yoga_without_feedback(self):
		self.s.ALTextToSpeech.say("Let's start the yoga session!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.perform_pose(pose)
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			time.sleep(5)

	def _yoga_with_feedback(self):
		self.s.ALTextToSpeech.say("Let's start the yoga session with feedback!")
		for pose in self.poses:
			if self.stop_flag:
				break
			self.perform_pose(pose)
			self.s.ALTextToSpeech.say(f"Now, {pose} pose.")
			time.sleep(5)
			self.provide_feedback(pose)

	def _perform_pose(self, pose):
		pass

	def _provide_feedback(self, pose):
		pass

if __name__ == "__main__":
	naoYogaInstructor = NaoYogaInstructor()
	naoYogaInstructor.start(feedback=True)
