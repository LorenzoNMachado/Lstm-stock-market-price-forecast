# Política de segurança

## Versões mantidas

Somente a branch `main` recebe manutenção. Não há versões publicadas ou
branches de release com suporte de segurança separado. O experimento declara
compatibilidade com Python 3.10–3.12; o CI confere a resolução das dependências
nessas versões, mas não executa o treinamento completo.

## Como reportar uma vulnerabilidade

Use **Security → Advisories → Report a vulnerability** na página deste
repositório para enviar um relato privado. Não abra uma issue pública nem
publique detalhes de exploração antes de conversar em privado com o mantenedor.
Inclua o arquivo e o contexto afetados e passos mínimos para reproduzir; não
inclua tokens, credenciais ou dados pessoais.

O projeto é mantido como portfólio e experimento educacional; não há prazo de
resposta ou garantia de correção. Issues públicas podem ser usadas para
problemas que não sejam vulnerabilidades.

## Escopo e limites

Relatos relevantes incluem credenciais expostas, dependências vulneráveis,
carregamento inseguro de arquivos externos e riscos em workflows. A previsão é
educacional e não constitui recomendação financeira. Os scanners e as
verificações estáticas não constituem garantia de segurança.

## Escopo do CI

O CI valida o JSON dos notebooks, analisa a sintaxe das células do V4 e roda
Bandit sobre uma exportação temporária das células, sem executar o experimento.
CodeQL não está configurado porque a implementação do modelo existe somente em
notebooks; analisar apenas o script auxiliar do CI daria cobertura limitada
sem alcançar o código principal do experimento.
