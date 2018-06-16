def solution(sticker):
    answer_1 = sticker[:-1]+[0]
    answer_2 = [0]+sticker[1:]
    sticker.reverse()
    answer_3 = sticker[:-1]+[0]
    answer_4 = [0]+sticker[1:]
    
    split_len = len(sticker)
    
    if len(sticker) < 3:
        return max(sticker)
    
    for idx in range(2, split_len):
        answer_1[idx] = max(answer_1[idx-1], answer_1[idx-2]+answer_1[idx])
        answer_2[idx] = max(answer_2[idx-1], answer_2[idx-2]+answer_2[idx])
        answer_3[idx] = max(answer_3[idx-1], answer_3[idx-2]+answer_3[idx])
        answer_4[idx] = max(answer_4[idx-1], answer_4[idx-2]+answer_4[idx])
        
    return max(answer_1[split_len-1], answer_2[split_len-1], answer_3[split_len-1], answer_4[split_len-1])