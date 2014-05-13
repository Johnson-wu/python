# -*- coding:utf-8 -*-
 
# from mytictoc import tic, toc
 
# big intiger multiplication
def bigmul(a,b):
    sa = str(a)
    sb = str(b)
    resultline = ' '*(len(sa)+len(sb))
 
    #   a
    # * b
    print
    print(resultline[:-len(sa)]+sa)
    print('*'+resultline[:-len(sb)-1]+sb)
 
    # ---
    print('-'*(len(sa)+len(sb)))
 
    #   ###
    #  ###
    # ###
    result_list = []
    cursp = 0
    for db in sb[::-1]:
        if int(db)==0:
            result = '0'*len(sa)
        else:
            result = ''
            carrier = 0
            for da in sa[::-1]:
                #print db,da
                mr = int(db)*int(da)+carrier
                carrier = mr/10
                result += str(mr%10)
            if carrier!=0:
                result += str(carrier)
        result = result[::-1]+' '*cursp
        cursp += 1
        result_list.append(resultline[:-len(result)]+result)
        print(result_list[-1])
 
    # ----
    print('-'*(len(sa)+len(sb)))
 
    # result
    print(str(sum([int(x.replace(' ','0')) for x in result_list])))
 
# unit test
def main():
    a = 1234567890
    b = 123456709
 
    # tic()
    bigmul(b,a)
    # toc()
 
    # tic()
    # bigmul(a,b)
    # toc()
 
if __name__=='__main__':
    main()