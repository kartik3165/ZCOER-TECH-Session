# student management system
dictnery = {
    "Ghanashyam Milind Ahire" : {"age" : 20 , "marks" : 85 },
    "Chetan kolhe" : { "age" : 22 , "marks" : 90},
    "Anuj Dhole" : { "age" : 21 , "marks" : 88},
    "Jivan Dhatbale" : { "age" : 22 , "marks" : 97},
    "Mohan Dinkar" : { "age" : 22 , "marks" : 96},
    "Mahesh Navale" : { "age" : 22 , "marks" : 93},
}
print(dictnery)
newstudent = input("Enter the New Student in Dictonery : ")
dictnery.update(newstudent)