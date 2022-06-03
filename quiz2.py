print("-Menu-")

print (" Digite 1 para para Quiz sobre Espiral. \n Digite 2 para o Quiz sobre FDD \n Digite 3 para sair.")

answer_user = input("Digite o número que você deseja:")

if answer_user == '1':
    print ("Quiz sobre scrum:")

    score = 0

    print("Começando...")
    print("1)1.	No modelo espiral de Boehm, o processo de software é representado como uma espiral e não como uma sequência \n"
          "de atividades com retornos de uma para outra. O modelo espiral de Boehm é \n "
           "A)um framework de processo de software dirigido a riscos. \n "
           "B)dividido em três setores: definição de objetivos, desenvolvimento e planejamento. \n "
           "C)pouco tolerante a mudanças ao longo do processo de software. \n "
           "D)construído de forma que a volta mais externa define o início do processo de software. \n ")

    answer_1 = input("Resposta: ")

    if answer_1 == "A":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")

    print(
        "2.O Modelo Espiral (Spiral) foi originalmente proposto por Boehm (1986) e é fortemente orientado à redução de riscos. \n"
        "WAZLAWICK, R. S. Engenharia de Software: Conceitos e práticas. São Paulo: Elsevier, 2013. \n"
        "\n Considerando o exposto e o Modelo Espiral de ciclo de vida de software, assinale a alternativa correta. "
        "A) O Modelo Espiral realiza uma etapa de cada vez, partindo para a próxima etapa apenas após a anterior estar totalmente validada.\n "
        "B) Tal modelo de ciclo de vida tem foco apenas na resolução de riscos de requisitos mal compreendidos, fornecendo tempo suficiente \n"
        "para que estes possam ser entendidos e implementados.\n "
        "C) O projeto é dividido em subprojetos, cada qual abordando um ou mais elementos de alto risco, até que todos os riscos identificados tenham sido tratados. \n "
        "D) Cada iteração é iniciada sem planejamento prévio, resolvendo-se os problemas no momento em que surgem.\n ")

    answer_2 = input("Resposta: ")

    if answer_2 == "C":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")

    print(
        "3. O processo de desenvolvimento de software conhecido como modelo em espiral (Modelo espiral de Boehm), divide cada volta da espiral \n"
        " em quatro setores, sendo um destes setores denominado de:"
        "A) estudos de caso.\n "
        "B) refatoração.\n "
        "C) setor administrativo.\n"
        "D) definição de objetivos.\n ")

    answer_3 = input("Resposta: ")

    if answer_3 == "D":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")

    print(
        "4.	O modelo em espiral de desenvolvimento proposto por Boehm apresenta a análise de riscos como uma das suas fases essenciais. \n"
        "C)CERTO \n" 
        "E)ERRADO \n ")

    answer_4 = input("Resposta: ")

    if answer_4 == "C":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")


    print(
        "5.O modelo espiral de Boehm foi criado em:\n"
        "A)1988 \n" 
        "B)2000\n"
        "C)1995 \n"
        "d)1967")

    answer_5 = input("Resposta: ")

    if answer_5 == "A":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")

elif answer_user == "2":
    print("Quiz sobre FDD")

    score = 0

    print("Começando...")

    print(
        "A Feature Driven Development (FDD) é uma metodologia ágil de desenvolvimento de software, sobre a qual é correto afirmar:"
        "\n A)Não pode ser combinada a outras técnicas para a produção de sistemas. \n "
        "B)Possui cinco processos: Desenvolver um Modelo Abrangente, Construir a Lista de Funcionalidades, Planejar por Funcionalidade,\n"
        " Detalhar por Funcionalidade e Implementar por Funcionalidade. \n "
        "C)Divide os papéis em dois grupos: papéis chave e papéis de apoio. Dentro de cada categoria, os papéis são atribuídos \n"
        " a um único participante que assume a responsabilidade pelo papel. \n "
        "D)Mantém seu foco apenas na fase de modelagem. ")
    answer_1 = input("Resposta: ")

    if answer_1 == 'B':
        print("Correto")
        score = score + 1
    else:
        print("Incorreto")
    print(""
        "2. O FDD (feature driven development) tem como principal característica fornecer uma maneira de construir e manter sistemas \n"
         "que satisfazem restrições de prazo, por meio do uso de prototipagem incremental em um ambiente controlado de projeto.\n"
        "C)CERTO \n"
        "E)ERRADO\n")
    answer_2 = input("Resposta: ")

    if answer_2 == 'E':
        print("Correto")
        score = score + 1
    else:
        print("Incorreto")

    print("3.Feature Driven Development (FDD) é uma das metodologias de desenvolvimento ágil, criada nos anos 90, por Jeff De Luca e Peter Coad, \n"
          " sendo robusta e também muito utilizada nos dias atuais. A FDD recomenda um conjunto de boas práticas que devem ser seguidas com sua utilização.\n"
          " Uma delas denota que os desenvolvedores devem sempre reconstruir o software, ou seja, ativar as funcionalidades e modificações realizadas”. Assinale-a.\n"
          "A)Entregas regulares (builds). \n"
          "B)Formação de equipe de projeto.\n"
          "C)Modelagem de objetos do domínio.\n"
          "d)Desenvolvimento por funcionalidade (feature).\n")
    answer_3 = input("Resposta: ")

    if answer_3 == 'A':
        print("Correto")
        score = score + 1
    else:
        print("Incorreto")

    print("4.O Feature Driven Development − FDD é uma metodologia ágil de desenvolvimento de software que\n"
          "A)Divide o processo de desenvolvimento nas etapas de Planejamento, Construção, Implantação e Manutenção. \n"
          "B)Normalmente possui papéis definidos relacionados ao desenvolvimento, como Gerente de Projeto, Testador etc.\n"
          "C)Usa a propriedade coletiva do código, ou seja, o código não tem um dono definido.\n"
          "d)Está associado a práticas de modelagem estruturada, não orientada a objetos do domínio.\n")
    answer_4 = input("Resposta: ")

    if answer_4 == 'B':
        print("Correto")
        score = score + 1
    else:
        print("Incorreto")


    print("5) FDD (Feature Driven Development) é uma metodologia muito objetiva, possuindo apenas duas fases: \n"
          "A)Concepção & Planejamento e Construção. \n"
          "B)Decomposição Funcional e Construção.\n"
          "C)Análise dos Requisitos e Desenvolvimento.\n"
          "d)Planejamento Incremental e Desenvolvimento por Funcionalidade.\n")
    answer_5 = input("Resposta: ")

    if answer_5 == 'A':
        print("Correto")
        score = score + 1
    else:
        print("Incorreto")
else:
    quit()

    print(f"Quiz acabou...Pontuação: {score}/5")
