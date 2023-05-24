# Python-To-do-List

## Lista de Taredas, salvando dados em JSON

## A lista conta com as ações undo (desfazer) e redo (refazer), que como os próprios nomes dizem, desfazem e refazem as últimas ações feitas pelo usuário. Funcionam com a presença de uma array secundário, que armazena os itens deletados e/ou adicionados na lista principal, que quando chamado, retorna os itens para a lista.

## O sistemas conta também com duas funções para salvar e importar os arquivos do documento .JSON. A função 'loadjson' importa os dados do arquivo para dentro do programa, na variável 'data', e cria um arquivo caso esse ainda não exista. Já a função 'savejson' exporta os arquivos da variável 'data' de volta ao arquivo .JSON.
