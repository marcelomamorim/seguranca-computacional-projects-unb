import random       
#random.SystemRandom() is used to generate random numbers from sources provided by the operating system.
import time


dice = random.SystemRandom() # A single dice.

def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
        
    if pow(a, exp, n) == 1:
        return True
        
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
            
        exp <<= 1
        
    return False
    
def miller_rabin(n, k=40):
    """_summary_
    Args:
        n (_type_): _description_
        k (int, optional): _description_. Defaults to 40.
    Returns:
        _type_: test result (True or False)
    """    
    for i in range(k):
        a = dice.randrange(2, n - 1)
        if not single_test(n, a):
            return False 
    return True
    

def gen_prime(bits):
    startTime = time.time()
    while True:
                            # 1 << bits - 1 = 2 ** (bits - 1)   
        a = (dice.randrange(1 << bits - 1, 1 << bits) << 1) + 1   # Guarantees that a is odd. 
        if miller_rabin(a):
            print(f"Tempo Total: Completado em {time.time() - startTime} segundos.")
            return a
            

if __name__ == "__main__":
    p = gen_prime(1024)
    print(p)
    
    """exemplo de output:
    603481458931529714217161781483451612328245174841413801327074983844349697754945215520503307803223688
    79442651038199948752441155654849617115444662495655489333012561094220861872003863512259410957877245
    046214227167553623496927441372168464010862629376074149090273763973086394724794550592791255128736977
    016680129350503843068298542544748258305526992726639612595404647758763211379002621787448307699633354
    873238476299545871825703804718603598206870348775275909690587000228938441152506961112452910257427170
    820121609010263773364420632186907868199518989689015288712535925118551003328614138517665496510242447
    001785916221043388104127
    """