def spam():
    #unused eggs
    #eggs =  'spam local'
    print('eggs')

def bacon():
    eggs = 'dacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'glocal'
bacon()
print(eggs)

#result
#bacon local
#spam local
#bacon local 
#global
