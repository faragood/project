def spy_game(nums):
    w = True
    state = 0
    for i in range(0, len(nums)):
        if nums[i] == 0 and state == 0:
            state+=1
        if nums[i] == 0 and state == 1:
            state+=1
        if nums[i] == 7 and state == 2:
            print(True)
            w = False
    if w:
        print(False)
        
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
