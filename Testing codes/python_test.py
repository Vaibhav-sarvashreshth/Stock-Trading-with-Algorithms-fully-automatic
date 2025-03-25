def new_tar_sl(tar , sl):
    l_per =0.2
    p_per = 0.09
    new_tar =  (tar /100)*(100+l_per)
    new_sl= (tar/100)*(100-(p_per))
    return {new_tar , new_sl}

print(new_tar_sl(100.2,99.91))