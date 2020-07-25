school = {}


def add_school(name,location,principal):
    school[name]={}
    school[name]["location"] = location
    school[name]["principal"] = principal
    school[name]["classes"] = {}
    school[name]["domrs"] = {}
    return school


def add_class(school_name, class_id, teacher):
    school[school_name]["classes"][class_id] = {}
    school[school_name]["classes"][class_id]["teacher"] = teacher
    school[school_name]["classes"][class_id]["students"] = {}
    return school


def add_student(school_name, class_id, id_num, name, dob): 
    school[school_name]["classes"][class_id]["students"][id_num] = {}
    school[school_name]["classes"][class_id]["students"][id_num]["name"]=name
    school[school_name]["classes"][class_id]["students"][id_num]["dob"] = dob
    return school

def get_school(name):
    g_school = school[name]
    return_d = {
        "school name":name,
        "location":g_school['location'],
        'principal': g_school['principal']
    }
    return return_d

def get_schools(location):
    results = []
    for key, value in school.items():
        if value['location'] == location:
            return_d = {
                "school name":key,
                "location":value['location'],
                'principal': value['principal']
    }
            results.append(return_d)
            
    return results
            
    

def get_classes(school_name):
    return school[school_name]["classes"]

def get_class(school_name, class_id):
    return school[school_name]["classes"][class_id]

def get_student():
    pass


add_school("kibra primary", "Kibra", "Mr")
add_school("olympic primary", "Olympic", "Mrs")
add_class('olympic primary', '1 red', 'Tc')
add_student('olympic primary', '1 red', 1003, "T M", '1995-12-1')
add_student('olympic primary', '1 red', 1003, "M M", '1995-12-1')
add_student('olympic primary', '1 red', 1005, "T M", '1995-12-1')
# print(get_school('olympic primary'))
# print(get_schools("Olympic"))
print(get_class('olympic primary','1 red'))