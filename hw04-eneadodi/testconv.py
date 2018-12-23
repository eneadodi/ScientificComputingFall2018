#!/usr/bin/env python3 
#-*- coding: utf-8 -*-





def main(local_argv):
    from convergent_sums import sum_1
    from convergent_sums import sum_2
    from convergent_sums import sum_3
    # storing first value in list of command line arguments for use in sequence
    # catching index error in case of no command line option
    try:
        n = float(local_argv[1])
    except IndexError:
        n = 1
    print(sum_1())
    print(sum_2())
    print(sum_3())
    
   
    
# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    from convergent_sums import sum_1
    from convergent_sums import sum_2
    from convergent_sums import sum_3
    import sys
    main(sys.argv)