from State import *
from Queue import PriorityQueue as PQ

def __main__():
	#start_state_array=[0,1,2,3,	4,5,6,7,	8,9,10,11,	12,13,14,15];
	#start_state_array=[0,2,10,3,	15,8,6,14,	5,13,1,7,	12,9,11,4];
	start_state_array=[9,14,15,10,	11,12,2,3,	4,0,1,13,	5,7,8,6];
	
	target_state_array=[1,2,3,4,	5,6,7,8,	9,10,11,12,	13,14,15,0];
	open_candidate_list=PQ(); #Put the candidate states
	closed_list={}; #dict(); #Dict, used to put the closed states

	start_state=State(start_state_array);
	start_state=cost_evaluated_state(start_state,	target_state_array);


	print("After Evaluation:");
	print(cost_evaluated_state(start_state, target_state_array).array);
	print("End Evaluation");


	open_candidate_list.put((start_state.f_dis, start_state));

	final_state=None;

	while(open_candidate_list.qsize()>0):
		cur_state_tuple=open_candidate_list.get();

		cur_state=cur_state_tuple[1];
		#print(cur_state.array);
		display(cur_state.array);

		# Put the closed states into the Dict
		closed_list[tuple(cur_state.array)]=cur_state;

		if cur_state.h_dis == 0:
			final_state=cur_state;
			break;

		#print("enter add childs");
		# Search tree implementation
		open_candidate_list = add_childs_to_openlist(cur_state, closed_list, open_candidate_list, target_state_array);
		#print("quit adding");
		print("open_candidate_list size:", open_candidate_list.qsize());

		

		#print(open_candidate_list);


	print("closed_list is ", closed_list);

	if final_state != None:
		print(final_state.f_dis);
	else:
		print("No path");

	


def display(state_arry):
	a=state_arry;
	for i in range(0,4):
		print a[i],a[i+1],a[i+2],a[i+3];




def cost_evaluated_state(cur_state,target_state_array):
	for index_cur in range(0,16):
		corr_index=-1;
		for index_tar in range(0,16):
			if target_state_array[index_tar]==cur_state.array[index_cur]:
				corr_index=index_tar;
				break;
		h_dis_x=((corr_index%4)-(index_cur%4)) if ((corr_index%4)-(index_cur%4))>0 else ((index_cur%4)-(corr_index%4));
		h_dis_y=((corr_index//4)-(index_cur//4)) if ((corr_index//4)-(index_cur//4))>0 else ((index_cur//4)-(corr_index//4));
		cur_state.h_dis=h_dis_x+h_dis_y;
		cur_state.f_dis+=cur_state.h_dis;
	return cur_state;


def add_childs_to_openlist(state, closed_list, open_candidate_list, target_state_array):
	zero_index=state.array.index(0);
	candidates=open_candidate_list;
	
	#print("zero index is ", zero_index);


	#for i in range(0,16):
	if zero_index//4-1 >= 0:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, (zero_index-4)%4),
						target_state_array
					);
		# Put the candidate into the open candidate list.
		if closed_list.has_key(tuple(new_state.array)) == False:
			new_state.parent_state=state;
			candidates.put((new_state.f_dis, new_state));

	if zero_index//4+1 <= 3:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, (zero_index+4)%4),
						target_state_array
					);
		# Put the candidate into the open candidate list.
		if closed_list.has_key(tuple(new_state.array)) == False:
			new_state.parent_state=state;
			candidates.put((new_state.f_dis, new_state));

	if zero_index%4-1 >= 0:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index-1),
						target_state_array
					);
		# Put the candidate into the open candidate list.
		if closed_list.has_key(tuple(new_state.array)) == False:
			new_state.parent_state=state;
			candidates.put((new_state.f_dis, new_state));

	if zero_index%4+1 <= 3:
		new_state = cost_evaluated_state(
						swap_ele(state, zero_index, zero_index+1),
						target_state_array
					);
		# Put the candidate into the open candidate list.
		if closed_list.has_key(tuple(new_state.array)) == False:
			new_state.parent_state=state;
			candidates.put((new_state.f_dis, new_state));

	return candidates;

def swap_ele(state, index_1, index_2):
	state.array[index_1], state.array[index_2]=state.array[index_2], state.array[index_1];
	return state;

__main__()