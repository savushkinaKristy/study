import random
bukbi="AEIOUBCDFGHJKLMNPQRSTVWXYZ"
zifri="0123456789"
simvoli="!@#$%^&*"
p_bukbi=random.choices(bukbi,k=3)
p_zifri=random.choices(zifri,k=3)
p_simvoli=random.choices(simvoli,k=3)
p=p_bukbi+p_zifri+p_simvoli
password=list(p)
random.shuffle(password)
password="".join(password)
print(password)