# -*- coding: utf-8 -*- 
from State import *
from Queue import PriorityQueue as PQ
from Queue import *
import copy
import heapq

#global
target_state_array = [0,	1,2,3,4,	5,6,7,8,	9,10,11,12,		13,14,15];
MaxDepth = 200;

def __main__():
	start_state_array = [1, 2, 6, 3,	4, 9, 5, 7,		8, 13, 11, 15,		12, 14, 0, 10]; #final

	closed_list = {}; #dict(); #Dict, used to put the closed states

	start_state = State(start_state_array);

	evaluate_state = cost_evaluated_state(start_state);

	open_candidate_list = [(evaluate_state.f_dis, evaluate_state.h_dis, evaluate_state)]; #Put the candidate states
	heapq.heapify(open_candidate_list);

	final_state = None;

	depth = 0;

	while(len(open_candidate_list) > 0):
		cur_state_tuple = heapq.heappop(open_candidate_list);

		cur_state = copy.deepcopy(cur_state_tuple[2]); #Get the state of the candidate, whose index is 2.   0: f_dis   1: h_dis

		# Put the closed states into the Dict
		closed_list[tuple(cur_state.array)] = cur_state;

		if cur_state.h_dis == 0:
			final_state = copy.deepcopy(cur_state);
			break;

		# Search tree implementation
		open_candidate_list = add_childs_to_openlist(cur_state, closed_list, open_candidate_list);

		check_queue = copy.deepcopy(open_candidate_list);

		depth +=1;
		print depth
		if depth == MaxDepth:
			break;

	if final_state != None:
		print("Found a path", final_state.f_dis);
	else:
		print("No path");

	show_back_route(final_state);




def show_back_route(state):
	if state.parent_state != None:
		show_back_route(state.parent_state);
	display(state.array);
	print "================="



def display(state_arry):
	a = state_arry;
	for i in range(0,4):
		print a[i*4], "\t", a[i*4+1], "\t", a[i*4+2], "\t", a[i*4+3];




def cost_evaluated_state(state):
	cur_state = copy.deepcopy(state);
	for index_cur in range(0,16):
		if cur_state.array[index_cur] == 0:
			continue;
		corr_index = -1;
		for index_tar in range(1,16):
			if target_state_array[index_tar] == cur_state.array[index_cur]:
				corr_index = index_tar;
				break;
		h_dis_x = abs((corr_index%4) - (index_cur%4));
		h_dis_y = abs((corr_index//4) - (index_cur//4));
		cur_state.h_dis += h_dis_x
		cur_state.h_dis += h_dis_y;
	cur_state.f_dis = cur_state.h_dis + cur_state.g_dis;
	return cur_state;


def add_to_openlist (new_state_in, parent_state_in, closed_list_in, open_candidate_list):
	new_state = copy.deepcopy(new_state_in);
	parent_state = copy.deepcopy(parent_state_in);
	candidates = copy.deepcopy(open_candidate_list);
	closed_list = closed_list_in.copy();
	# Put the candidate into the open candidate list.
	#if closed_list.has_key(tuple(new_state.array)) == False:
	if (tuple(new_state.array) not in closed_list.keys()):
		new_state.parent_state = parent_state;
		new_state.g_dis += 1;
		new_state.f_dis = new_state.g_dis + new_state.h_dis;
		heapq.heappush(candidates,(new_state.f_dis, new_state.h_dis, new_state));
	return candidates;
	# else:
	# 	return candidates;

def add_childs_to_openlist(state_in, closed_list_in, open_candidate_list):
	zero_index = state_in.array.index(0);
	candidates = copy.deepcopy(open_candidate_list);
	closed_list = closed_list_in.copy();

	cur_state = copy.deepcopy(state_in); # keep transfered state as cur_state
	cur_state.h_dis = 0; #重置子节点的h_dis

	# Move Down	
	state = copy.deepcopy(cur_state);
	if zero_index//4 + 1 <= 3:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index + 4)
					);
		candidates = add_to_openlist (new_state, state, closed_list, candidates);	

	# Move Right
	state = copy.deepcopy(cur_state);
	if zero_index%4 + 1 <= 3:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index + 1)
					);
		candidates = add_to_openlist (new_state, state, closed_list, candidates);

	# Move Up
	state = copy.deepcopy(cur_state);
	if zero_index//4 - 1 >= 0:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index - 4)
					);
		candidates = add_to_openlist (new_state, state, closed_list, candidates);

	# Move Left
	state = copy.deepcopy(cur_state);
	if zero_index%4 - 1 >= 0:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index - 1)
					);
		candidates = add_to_openlist (new_state, state, closed_list, candidates);

	return candidates;


def swap_ele(state_come, index_1, index_2):
	n_state = copy.deepcopy(state_come);
	n_state.array[index_1], n_state.array[index_2] = n_state.array[index_2], n_state.array[index_1];
	return n_state;


def check_dupli(queue_in):
	queue = copy.deepcopy(queue_in);
	qsize = len(queue);
	list_temp = {};
	while (len(queue) > 0):
		q = heapq.heappop(queue);
		list_temp[tuple(q[2].array)] = q[2];
	list_size = len(list_temp);
	print "Queue size: ", qsize;
	print "List Size: ", list_size;
	if qsize == list_size:
		return False;
	elif qsize > list_size:
		return True;
	else:
		return -1;
__main__()
