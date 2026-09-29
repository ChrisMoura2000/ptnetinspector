[
  {
    "codigo": "802-1X",
    "nome": "802.1X / EAPOL",
    "descricao": "Verifica o comportamento da rede perante mecanismos de autenticação 802.1X.",
    "deteccao": "Envia mensagens EAPOL e analisa as respostas dos dispositivos.",
    "risco": "alto",
    "ip_version": "L2"
  },
  {
    "codigo": "4-LLMNR",
    "nome": "LLMNR IPv4",
    "descricao": "Verifica se dispositivos respondem a consultas LLMNR através de IPv4.",
    "deteccao": "Envia consultas LLMNR multicast IPv4 e analisa as respostas recebidas.",
    "risco": "medio",
    "ip_version": "IPv4"
  },
  {
    "codigo": "4-MDNS",
    "nome": "mDNS IPv4",
    "descricao": "Verifica a utilização e exposição de serviços através de Multicast DNS em IPv4.",
    "deteccao": "Envia ou observa consultas mDNS multicast IPv4 e analisa as respostas.",
    "risco": "medio",
    "ip_version": "IPv4"
  },
  {
    "codigo": "4-MULTIECHO",
    "nome": "Multiple ICMP Echo",
    "descricao": "Verifica o comportamento dos dispositivos diante de múltiplas solicitações ICMP Echo.",
    "deteccao": "Envia solicitações ICMP Echo e analisa as respostas dos dispositivos.",
    "risco": "baixo",
    "ip_version": "IPv4"
  },
  {
    "codigo": "6-LLMNR",
    "nome": "LLMNR IPv6",
    "descricao": "Verifica se dispositivos respondem a consultas LLMNR através de IPv6.",
    "deteccao": "Envia consultas LLMNR multicast IPv6 e analisa as respostas recebidas.",
    "risco": "medio",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-MDNS",
    "nome": "mDNS IPv6",
    "descricao": "Verifica a utilização e exposição de serviços através de Multicast DNS em IPv6.",
    "deteccao": "Envia ou observa consultas mDNS multicast IPv6 e analisa as respostas.",
    "risco": "medio",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-MLDV1",
    "nome": "MLDv1",
    "descricao": "Verifica o comportamento dos dispositivos perante mensagens Multicast Listener Discovery versão 1.",
    "deteccao": "Executa testes MLDv1 e analisa as respostas e memberships multicast.",
    "risco": "medio",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-MLDV2",
    "nome": "MLDv2",
    "descricao": "Verifica o comportamento dos dispositivos perante mensagens Multicast Listener Discovery versão 2.",
    "deteccao": "Envia mensagens MLDv2 e analisa respostas e memberships multicast.",
    "risco": "medio",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-OUTRANGE",
    "nome": "ICMPv6 Out-of-Range",
    "descricao": "Verifica respostas inadequadas a determinados tráfegos ICMPv6 fora do contexto esperado.",
    "deteccao": "Envia probes ICMPv6 específicas e analisa o comportamento dos dispositivos.",
    "risco": "medio",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-FAKERA",
    "nome": "Fake Router Advertisement",
    "descricao": "Verifica se dispositivos aceitam Router Advertisements IPv6 não autorizados.",
    "deteccao": "Emula um roteador IPv6 e envia Router Advertisements falsos para observar o comportamento dos hosts.",
    "risco": "alto",
    "ip_version": "IPv6"
  },
  {
    "codigo": "6-FAKERADNS",
    "nome": "Fake Router Advertisement + DNS",
    "descricao": "Verifica se um Router Advertisement falso consegue anunciar um servidor DNS controlado.",
    "deteccao": "Envia Router Advertisement contendo uma configuração DNS especificada e observa a reação dos hosts.",
    "risco": "alto",
    "ip_version": "IPv6"
  }
]