    
# Jason Pren
# CMIS -120
## 13.June.2022
def greeting(string):
   title = 'earth mass / earth gravity(9.81)  moon gravity(1.62) = the lunar mass'
   return(title)
    

def query_user(*args,**kwargs):
    earth_mass = int(input("Please enter a weight: "))
    earth_minus_gravity = earth_mass / 9.80
    print(earth_minus_gravity * 1.16, ' Is the mass on the moon') 
 
     

def lunar_calc(*earth_force, earth_mass) ->float :
    calculated_weight = (float(earth_mass) / float(earth_force))
    print(calculated_weight, 'Would be the mass if your were on the mooon...')




def main():
    query_user()
   
   
    
main()

