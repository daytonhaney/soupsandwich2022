git remote set-url origin git@github.com:username/repo.gitfrom datetime import date
import yaml


class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name},age={self.age}'


p1 = Person('Jim Peters', date(1929,10,23))
p2 = Person('Michael Palin', date(1934,3,1))


print(yaml.dump({'john': p1, 'michael':p1})

yaml_data = '''
john: !!python/object:__main__.Person
    age: 1929-10-23
    name: Jim Peters
michael: !!python/object:__main__.Person
    age: 1934-3-1
    name: Michael Palin 
'''
yaml.load(yaml_data)


yaml_data1 = '''
exec_paths:
    !!python/object/apply:os.get_exec_path []
exec_command:
    !!python/object/apply:subprocess.cgithub.com/runtimejpp/soupsandwich2022heck_output [['ls','/']]
'''
yaml.load(yaml_data1)
