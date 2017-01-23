def get_sliced_lists(nums):
  ex_last_lst = nums[:-1]
  ex_fir_last_lst = nums[1:-1]
  rev_lst = nums[::-1]
  lists = [ex_last_lst,ex_fir_last_lst,ex_fir_last_lst,rev_lst]
  
  return lists
