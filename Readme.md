

# Poetry

- Create venv for poetry
- activate poetry environment
- pip install poetry
- In PyCharm: Create new project venv (using poetry)
  - Python: Base auswählen
  - Pfad zu poetry.exe auswählen
- in pyproject.toml: ```package-mode = false```
- Installiere Pakete
  - Existing project: ```poetry install``` (installiert alle dependencies in pyproject.toml)
  - New project: ```poetry add <package>```

# NEO4J

- Download NEO4J Desktop or Use Cloud Version (https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)
- Change neo4j.conf

Path to conf: e.g. ```C:\Users\user\.Neo4jDesktop2\Data\dbmss\dbms-850417bd-1c53-4b40-859a-a2324da08cba\conf```

```bash
dbms.security.procedures.unrestricted=my.extensions.example,my.procedures.*,algo.*,apoc.*
dbms.security.procedures.allowlist=apoc.*
```
