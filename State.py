class State:
	def __init__(self,array):
		self.g_dis=0;
		self.h_dis=0;
		self.f_dis=0;
		self.array=array;
		self.parent_state=None;