from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', prox="/introducao")

@app.route('/introducao')
def introducao():
    return render_template('introducao.html', prox="/sprint", ante="/")

@app.route('/sprint')
def sprint():
    return render_template('sprint.html', prox="/sprintbacklog", ante="/introducao")

@app.route('/sprintbacklog')
def sprintbacklog():
    return render_template('SprintBacklog.html', prox="/mvp", ante="/sprint")

@app.route('/mvp')
def mvp():
    return render_template('mvp.html', prox="/po", ante="/sprintbacklog")


@app.route('/po')
def po():
    return render_template('po.html', prox="/sm", ante="/mvp")

@app.route('/sm')
def sm():
    return render_template('sm.html', prox="/equipe", ante="/po")

@app.route('/equipe')
def equipe():
    return render_template('equipe.html', prox="/productbacklog", ante="/sm")

@app.route('/productbacklog')
def pbacklog():
    return render_template('productbacklog.html', prox="/dor-dod", ante="/equipe")

@app.route('/dor-dod')
def dor_dod():
    return render_template('dor-dod.html', prox="/burndown", ante="/productbacklog")

@app.route('/burndown')
def burndown():
    return render_template('burndown.html', prox="/planningpoker", ante="/dor-dod")

@app.route('/planningpoker')
def PP():
    return render_template('planningpoker.html', prox="/skills", ante="/burndown")

@app.route('/skills')
def skills():
    return render_template('shskills.html', prox="/materiaisextras", ante="/planningpoker")

@app.route('/materiaisextras')
def materiaisextras():
    return render_template('materiaisextras.html', prox="/", ante="/skills")

@app.route('/audios')
def audios():
    return render_template('audios.html', ante="/")

@app.route('/questoes', methods=['GET', 'POST'])
def questoes():
    global Q
    global alt
    global gab
    score = 0
    if request.method == 'POST':
        resp=[] #respostas
        for i in range(0,len(Q)):   #Checa cada alternativa e compara com gabarito
            resp.append(request.form[f'q{i}'])
            if request.form[f'q{i}'] == gab[i]:
                score += 1    
        scorep = score/len(Q)*100   #porcentagem de acertos
        return render_template('questoes.html', q = Q, alt = alt, x = len(Q), score = score, scorep = int(scorep), enviado = True, gab = gab, resp = resp)
    return render_template('questoes.html', q = Q, alt = alt, x = len(Q), enviado = False, gab = gab)

Q = ['O que é o Scrum?',
'Quais são os principais benefícios do uso do Scrum em um projeto?',
'Em qual(is) das seguintes áreas o Scrum pode NÃO é aplicado comumente?',
'Qual é o principal passo inicial que deve ser tomado para começar a aplicar o Scrum de forma eficaz?',
'Como o Scrum lida com mudanças nos requisitos do projeto?',
'Qual é a finalidade do Product Backlog no Scrum?',
'Qual é a duração típica de uma sprint no Scrum?',
'O que é um Sprint Backlog no Scrum?',
'Qual é o principal artefato utilizado no Scrum para representar as funcionalidades e requisitos do produto?',
'Qual é o artefato do Scrum que representa o trabalho a ser realizado durante a sprint atual?',
'Qual é o artefato do Scrum que mostra o progresso do trabalho ao longo do tempo durante uma sprint?',
'Qual é o artefato do Scrum que representa o produto funcional e entregável ao final de cada sprint?',
'Qual é o objetivo do Product Backlog no Scrum?',
'Qual das seguintes opções descreve corretamente o Product Backlog no Scrum?',
'Qual é o principal propósito do Burndown no Scrum?',
'O que é o Incremento no Scrum?',
'Qual é o objetivo do Daily Scrum no Scrum?',
'Qual é o objetivo de uma retrospectiva no Scrum?',
'O que acontece durante o Daily Scrum no Scrum?',
'Qual é o propósito da Sprint Retrospective no Scrum?',
'O Daily Scrum é um evento de coordenação diária que permite que a equipe inspecione o progresso em relação ao objetivo da sprint. Qual é o tempo máximo recomendado para a duração do Daily Scrum?',
'Durante o Sprint Review, a equipe do Scrum apresenta o incremento do produto aos clientes para obter feedback. Qual é o principal objetivo do Sprint Review?',
'A Sprint Retrospective é um momento de inspeção e adaptação, em que a equipe do Scrum reflete sobre o último sprint e identifica melhorias no processo. Qual é a principal diferença entre uma Sprint Retrospective eficaz e uma reunião de status?',
'Qual é o papel do Product Owner no Scrum?',
'Qual das seguintes opções NÃO é um papel no Scrum?',
'Qual é o papel do Scrum Master no Scrum?',
'Qual é a principal responsabilidade do Product Owner no Scrum?',
'Qual é a principal responsabilidade da equipe de desenvolvimento no Scrum?',
'Qual é o tamanho ideal da equipe de desenvolvimento no Scrum?',
'Qual é a principal diferença entre o Product Owner e o Scrum Master?',
'Qual é o papel do Scrum Master em relação aos clientes externos ao time Scrum?',
'Qual é a principal responsabilidade do Product Owner em relação à qualidade do produto?',
'Como o Scrum Master pode promover a colaboração e a auto-organização da equipe de desenvolvimento?',
'Qual é a principal responsabilidade da equipe de desenvolvimento em relação à qualidade do produto?',
'Quais são as principais habilidades e conhecimentos necessários para um Scrum Master eficaz?',
'Qual das seguintes habilidades é considerada uma soft skill?',
'Qual das seguintes habilidades é considerada uma hard skill?',
'Qual das seguintes habilidades é considerada uma soft skill?',
'Qual das seguintes habilidades é considerada uma hard skill?',
'Qual das seguintes habilidades é considerada uma soft skill?',
'Qual das seguintes habilidades é considerada uma soft skill que envolve a capacidade de lidar com a ambiguidade, incerteza e complexidade?',
'Qual das seguintes habilidades é considerada uma hard skill que envolve a capacidade de analisar grandes conjuntos de dados e extrair informações relevantes?',
'Qual das seguintes habilidades é considerada uma soft skill que envolve a capacidade de influenciar e persuadir os outros de forma ética?',
'Qual das seguintes habilidades é considerada uma hard skill que envolve a capacidade de projetar e desenvolver software de alta qualidade?',
'Qual das seguintes habilidades é considerada uma soft skill que envolve a capacidade de se adaptar rapidamente a novas situações e mudanças?']


alt = [['Um método ágil para gerenciamento de projetos.',
'Uma linguagem de programação.',
'Um método para testes de software.',
'Um modelo de negócio para startups.'],

['Maior previsibilidade e transparência.',
'Maior qualidade e satisfação do cliente.',
'Maior adaptabilidade a mudanças.',
'Todas as alternativas anteriores.'],

['Desenvolvimento de software e TI.',
'Gerenciamento de projetos.',
'Marketing e publicidade.',
'Saúde e medicina.'],

['Identificar as necessidades e expectativas dos clientes.',
'Realizar uma análise detalhada dos processos existentes.',
'Treinar e capacitar a equipe em todos os aspectos do Scrum.',
'Contratar um consultor especializado em implementação de Scrum.'],

['Registrando as mudanças para avaliação futura.',
'Priorizando as mudanças antes do início da sprint.',
'Adicionando as mudanças como itens no Product Backlog.',
'Ignorando as mudanças até o próximo planejamento do projeto.'],

['Rastrear o progresso diário das tarefas.',
'Priorizar as histórias de usuário.',
'Planejar as atividades diárias do time.',
'Estimar o tempo necessário para cada tarefa.'],

['1 semana.',
'2 - 3 semanas.',
'4 - 5 semanas.',
'Depende do tamanho do projeto.'],

['Uma lista ordenada de funcionalidades a serem desenvolvidas.',
'Uma ferramenta para rastrear o progresso do projeto.',
'Um relatório com as lições aprendidas do sprint anterior.',
'Uma lista de tarefas selecionadas para a sprint atual.'],

['Product Backlog.',
'Sprint Backlog.',
'Burndown.',
'Incremento.'],

['Product Backlog.',
'Sprint Backlog.',
'Burndown.',
'Incremento.'],

['Product Backlog.',
'Sprint Backlog.',
'Burndown.',
'Incremento.'],

['Product Backlog.',
'Sprint Backlog.',
'Burndown.',
'Incremento.'],

['Priorizar as tarefas a serem realizadas durante a sprint.',
'Mostrar o progresso do trabalho ao longo do tempo.',
'Representar as funcionalidades e requisitos do produto.',
'Refletir o trabalho realizado durante a sprint atual.'],

['Uma lista ordenada de tarefas que precisam ser concluídas durante uma sprint.',
'Um conjunto de itens selecionados para serem trabalhados durante o próximo sprint.',
'Uma lista de funcionalidades e requisitos do produto, priorizada e em constante evolução.',
'Um artefato que mostra o progresso do trabalho ao longo do tempo durante uma sprint.'],

['Acompanhar o progresso diário das tarefas da equipe.',
'Registrar as lições aprendidas e os principais marcos alcançados.',
'Identificar os impedimentos e problemas enfrentados pela equipe.',
'Visualizar o progresso do trabalho e a quantidade de trabalho restante ao longo do tempo durante uma sprint.'],

['Uma lista de tarefas selecionadas para a sprint atual.',
'Um relatório que registra o trabalho realizado durante a sprint atual.',
'O produto funcional e entregável ao final de cada sprint.',
'Uma descrição detalhada das funcionalidades e requisitos do produto.'],

['Avaliar o progresso do projeto.',
'Revisar e ajustar o Product Backlog.',
'Realizar uma retrospectiva do sprint.',
'Sincronizar e planejar o trabalho diário.'],

['Planejar as atividades para a próxima sprint.',
'Avaliar o trabalho realizado no sprint.',
'Priorizar as histórias de usuário.',
'Identificar e remover impedimentos.'],

['Revisão e demonstração do incremento do produto.',
'Planejamento das atividades para a próxima sprint.',
'Atualização do Product Backlog com novos requisitos.',
'Coordenação diária entre os membros da equipe para discutir progresso e planejar o trabalho do dia.'],

['Planejar as atividades para a próxima sprint.',
'Revisar o trabalho realizado durante a sprint anterior.',
'Priorizar as histórias de usuário no Product Backlog.',
'Identificar melhorias no processo e ações para aprimorar a eficácia da equipe.'],

['15 minutos.',
'30 minutos.',
'45 minutos.',
'60 minutos.'],

['Demonstrar as funcionalidades concluídas durante a sprint.',
'Priorizar as histórias de usuário para a próxima sprint.',
'Obter feedback dos clientes sobre o trabalho realizado durante a sprint.',
'Planejar as atividades para a próxima sprint.'],

['Uma Sprint Retrospective foca em ações concretas para a melhoria contínua.',
'Uma reunião de status se concentra em relatar o progresso sem planejar melhorias.',
'Uma Sprint Retrospective é conduzida pelo Scrum Master, enquanto uma reunião de status é liderada pelo Product Owner.',
'Não há diferença significativa entre uma Sprint Retrospective e uma reunião de status.'],

['Gerenciar a execução diária do projeto.',
'Definir os requisitos e prioridades do produto.',
'Facilitar a comunicação e remoção de impedimentos.',
'Monitorar o progresso e a qualidade do projeto.'],

['Scrum Master.',
'Product Owner.',
'Sprint Planner.',
'Development Team.'],

['Gerenciar o Product Backlog e priorizar as histórias de usuário.',
'Facilitar o processo Scrum, remover impedimentos e ajudar a equipe a alcançar a auto-organização.',
'Ser o representante dos clientes e tomar decisões em nome deles.',
'Desenvolver o incremento do produto e garantir que as metas da sprint sejam atingidas.'],

['Definir as metas e o plano de trabalho para a sprint.',
'Coordenar as atividades diárias da equipe de desenvolvimento.',
'Gerenciar o backlog do produto, priorizar os itens e garantir o valor entregue.',
'Fornecer suporte técnico e orientação para a equipe de desenvolvimento.'],

['Definir o backlog do produto e priorizar as histórias de usuário.',
'Gerenciar o processo Scrum e garantir que as metas da sprint sejam atingidas.',
'Desenvolver o incremento do produto de acordo com as metas e requisitos definidos.',
'Representar os clientes e tomar decisões em nome deles.'],

['Pode variar dependendo do projeto, mas geralmente é entre 3 e 9 membros.',
'Deve ser composta por um número fixo de 7 membros.',
'Não há restrição de tamanho, podendo ser ajustada de acordo com as necessidades do projeto.',
'Deve incluir todos os membros da organização envolvidos no desenvolvimento do produto.'],

['O Product Owner é responsável pela facilitação do processo Scrum, enquanto o Scrum Master gerencia o backlog do produto.',
'O Product Owner prioriza as histórias de usuário, enquanto o Scrum Master remove os impedimentos e facilita o processo Scrum.',
'O Product Owner representa os clientes e toma decisões em nome deles, enquanto o Scrum Master coordena as atividades diárias da equipe.',
'O Product Owner é responsável pelo desenvolvimento do incremento do produto, enquanto o Scrum Master gerencia as metas da sprint.'],

['Representar os interesses dos clientes externos e tomar decisões em nome deles.',
'Facilitar a comunicação entre os clientes externos e a equipe de desenvolvimento.',
'Definir as metas e prioridades dos clientes externos.',
'Garantir que os clientes externos cumpram suas responsabilidades no Scrum.'],

['Desenvolver planos de teste abrangentes para garantir a qualidade do produto.',
'Definir critérios de aceitação claros para garantir a qualidade das histórias de usuário.',
'Garantir que a equipe de desenvolvimento siga as melhores práticas de desenvolvimento de software.',
'Priorizar as histórias de usuário de acordo com a sua complexidade técnica.'],

['Atribuindo tarefas específicas a cada membro da equipe.',
'Definindo metas individuais para cada membro da equipe.',
'Facilitando reuniões de brainstorming e incentivando a participação ativa de todos os membros da equipe.',
'Tomando decisões em nome da equipe para evitar conflitos e atrasos.'],

['Realizar testes rigorosos para identificar todos os defeitos do produto.',
'Documentar todos os problemas encontrados durante o desenvolvimento.',
'Garantir que todas as funcionalidades do produto sejam entregues no prazo.',
'Desenvolver um produto de alta qualidade, de acordo com os critérios de aceitação definidos pelo Product Owner.'],

['Habilidades técnicas avançadas e experiência em liderança de equipe.',
'Conhecimento aprofundado das práticas de desenvolvimento de software e habilidades de gerenciamento de projetos.',
'Habilidades de comunicação eficazes, facilitação de processos e resolução de conflitos.',
'Experiência prévia como Product Owner e habilidades analíticas avançadas.'],

['Programação em Python.',
'Resolução de problemas complexos.',
'Comunicação eficaz.',
'Conhecimento avançado de matemática.'],

['Empatia.',
'Criatividade.',
'Pensamento crítico.',
'Conhecimento de programação em C++.'],

['Gestão de projetos.',
'Análise de dados.',
'Negociação.',
'Conhecimento de estatística.'],

['Liderança.',
'Trabalho em equipe.',
'Raciocínio lógico.',
'Comunicação interpessoal.'],

['Conhecimento de ferramentas de design gráfico.',
'Solução de problemas complexos.',
'Pensamento analítico.',
'Inteligência emocional.'],

['Resiliência.',
'Pensamento sistêmico.',
'Gestão de tempo.',
'Conhecimento de linguagens de programação.'],

['Empatia.',
'Comunicação verbal.',
'Análise de dados.',
'Colaboração em equipe.'],

['Liderança.',
'Conhecimento técnico.',
'Criatividade.',
'Gestão de conflitos.'],

['Trabalho em equipe.',
'Pensamento crítico.',
'Conhecimento de linguagens de programação.',
'Flexibilidade cognitiva.'],

['Resolução de problemas.',
'Conhecimento de estatística.',
'Flexibilidade.',
'Pensamento analítico.']]

gab = ['A', 'D', 'D', 'C', 'C', 'B', 'B', 'D', 'A', 'B', 'C', 'D', 'C', 'C', 'D', 'C', 'D', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'B', 'C', 'C', 'A', 'B', 'B', 'B', 'C', 'D', 'C', 'C', 'D', 'C', 'C', 'D', 'B', 'C', 'A', 'C', 'C ']

app.run(debug=True)