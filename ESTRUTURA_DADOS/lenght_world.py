from datetime import datetime
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    
    
    def lengthOfLastWord_manual(self, s: str) -> int:
        last_espace = s.rfind(' ')
        if last_espace == -1:
            return 0
        print(s[last_espace+1:])
        return len(s[last_espace+1:])


s = """Em um mundo cada vez mais conectado, os dados se tornaram o novo petróleo. 
    Empresas e organizações dependem de informações precisas e atualizadas para tomar decisões estratégicas, 
    melhorar seus processos e oferecer produtos e serviços mais personalizados. 
    A engenharia de dados desempenha um papel fundamental nesse cenário, pois é responsável por coletar, 
    transformar e disponibilizar dados de diversas fontes, garantindo sua qualidade e integridade. 
    Profissionais dessa área precisam dominar linguagens de programação, ferramentas de integração e plataformas 
    de orquestração, como o Apache Airflow, que permite automatizar e monitorar pipelines de dados complexos. 
    Além disso, é essencial compreender conceitos de bancos de dados relacionais e não relacionais, 
    otimização de consultas SQL, modelagem dimensional e boas práticas de governança de dados. 
    À medida que a quantidade de informações continua crescendo exponencialmente, o papel do engenheiro de dados 
    se torna cada vez mais estratégico para o sucesso das organizações no mundo digital.
Em um mundo cada vez mais conectado, os dados se tornaram o novo petróleo. 
    Empresas e organizações dependem de informações precisas e atualizadas para tomar decisões estratégicas, 
    melhorar seus processos e oferecer produtos e serviços mais personalizados. 
    A engenharia de dados desempenha um papel fundamental nesse cenário, pois é responsável por coletar, 
    transformar e disponibilizar dados de diversas fontes, garantindo sua qualidade e integridade. 
    Profissionais dessa área precisam dominar linguagens de programação, ferramentas de integração e plataformas 
    de orquestração, como o Apache Airflow, que permite automatizar e monitorar pipelines de dados complexos. 
    Além disso, é essencial compreender conceitos de bancos de dados relacionais e não relacionais, 
    otimização de consultas SQL, modelagem dimensional e boas práticas de governança de dados. 
    À medida que a quantidade de informações continua crescendo exponencialmente, o papel do engenheiro de dados 
    se torna cada vez mais estratégico para o sucesso das organizações no mundo digital.
Em um mundo cada vez mais conectado, os dados se tornaram o novo petróleo. 
    Empresas e organizações dependem de informações precisas e atualizadas para tomar decisões estratégicas, 
    melhorar seus processos e oferecer produtos e serviços mais personalizados. 
    A engenharia de dados desempenha um papel fundamental nesse cenário, pois é responsável por coletar, 
    transformar e disponibilizar dados de diversas fontes, garantindo sua qualidade e integridade. 
    Profissionais dessa área precisam dominar linguagens de programação, ferramentas de integração e plataformas 
    de orquestração, como o Apache Airflow, que permite automatizar e monitorar pipelines de dados complexos. 
    Além disso, é essencial compreender conceitos de bancos de dados relacionais e não relacionais, 
    otimização de consultas SQL, modelagem dimensional e boas práticas de governança de dados. 
    À medida que a quantidade de informações continua crescendo exponencialmente, o papel do engenheiro de dados 
    se torna cada vez mais estratégico para o sucesso das organizações no mundo digital.
Em um mundo cada vez mais conectado, os dados se tornaram o novo petróleo. 
    Empresas e organizações dependem de informações precisas e atualizadas para tomar decisões estratégicas, 
    melhorar seus processos e oferecer produtos e serviços mais personalizados. 
    A engenharia de dados desempenha um papel fundamental nesse cenário, pois é responsável por coletar, 
    transformar e disponibilizar dados de diversas fontes, garantindo sua qualidade e integridade. 
    Profissionais dessa área precisam dominar linguagens de programação, ferramentas de integração e plataformas 
    de orquestração, como o Apache Airflow, que permite automatizar e monitorar pipelines de dados complexos. 
    Além disso, é essencial compreender conceitos de bancos de dados relacionais e não relacionais, 
    otimização de consultas SQL, modelagem dimensional e boas práticas de governança de dados. 
    À medida que a quantidade de informações continua crescendo exponencialmente, o papel do engenheiro de dados 
    se torna cada vez mais estratégico para o sucesso das organizações no mundo digital."""

solucao = Solution()

inicio =datetime.now()
print(solucao.lengthOfLastWord(s))
fim = datetime.now()
print(f'heashmap: {fim - inicio}')

inicio =datetime.now()
print(solucao.lengthOfLastWord_manual(s=s))
fim = datetime.now()
print(f'mydict: {fim - inicio}')

