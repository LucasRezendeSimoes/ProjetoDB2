#Aqui estão apenas algumas queries, cole-as em codigo.py para implementá-las

# Mostra histórico dos alunos
    for i in colecoes['Alunos'].find(): # Percorre a coleção de alunos

        if i['Nome'] == 'Jerry Summerson': # Procura por um dado e específico, comenta caso queira listar todos

            print('\nNome:', i['Nome'], "  RA:", i['RA'])
            print('{')
            for j in i['Hist']:
                print('\nNome da disciplina:', j['Nome_disc'])
                print('Id da disciplina:', j['Id_disc'])
                print('Semestre e ano: %d/%d', (j['Semestre'],j['Ano']))
                print('Nota final:', j['Nota'],'\n')
            print('}\n\n\n')
    
    # Mostra todas as disciplinas ministradas por professores

    for i in colecoes['Professores'].find():# Percorre a coleção de professores

        if i['Nome'] == 'Cléber': # Procura por um dado e específico, comenta caso queira listar todos
            
            print('\nNome:', i['Nome'])
            print('{')
            for j in i['Hist']:
                print('\nNome da disciplina:', j['Nome_disc'])
                print('Id da disciplina:', j['Id_disc'])
                print('Semestre e ano: %d/%d'%( j['Semestre'],j['Ano']))
            print('}\n\n\n')

    # Lista os alunos que já s formaram
    for i in colecoes['Alunos'].find(): # Percorre a coleção

        if i['Formado'] != 0: # Se o dado for 0, o aluno ainda não se formou

            print('Nome:', i['Nome'], "  RA:", i['RA'])
            print('Formado: %d/%d\n'%(i['Semestre'],i['Formado']))
    print('\n\n\n')

    # Lista todos os departamentos e seus coordenadores
    for i in colecoes['Departamentos'].find(): # Percorre a coleção
        print('Coordenador:', i['Coordenador']['Nome'], '  ID:', i['Coordenador']['Id'])
        print('Departamento:', i['Nome'], '  ID do departamento:', i['_id'],'\n')
    print('\n\n\n')

    # Lista todos os grupos de TCC
    g = 1
    for i in colecoes['TCC'].find(): # Percorre a coleção
        print('Grupo %d:'% g)
        print('Orientador:', i['Orientador']['Nome'], "  ID:", i['Orientador']['Id'])
        for j in i['Alunos']:
            print('Aluno:', j['Nome'], '  ','RA:',j['RA'])
        print()
        g+=1
