

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}



usuarios_machine_learning

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

set(assistiram)



for usuario in set(assistiram):
  print(usuario)




usuarios_data_science | usuarios_machine_learning


