Backend czy frontend?
Chleb kosztuje złotówkę i pół chleba ile koszuje cały chleb? 2zl
Jakie są Pana/Pani mocne i słabe strony?
Największy sukces w it?
Jak odnajdujesz się w zespole?

I. Ogólne:
1. Co to jest uwierzytelnianie a autoryzacja?
   Uwierzytelnianie - weryfikacja tożsamości użytkownika np. za pomocą hasła.
   Autoryzacja - prawo do wykonania konkretnej operacji/dostępu do konkretnego pliku

2. Jaka jest różnica między szyfrowaniem a haszowaniem?
   Szyfrowanie - proces zamiany tekstu jawnego (zrozumiałego dla człowieka) w szyfrogram.
   Haszowanie - wyliczenie przy użyciu funkcji skrótu ciągu znaków o stałej długości. Jest to proces nieodwracalny.
   - Jak przechowywać hasła użytkowników w bazie danych? Jak sprawdzić, czy plik nie został zmodyfikowany?

3. Co oznacza określenie API
   user - metody/params/response - api - requets/response - app
   a. Jaka jest różnica między usługami sieciowymi REST i SOAP (co to jest rest api)
   b. Wymień metody HTTP obsługiwane przez REST - get, post, put, delete
   c. Co to jest CRUD?
   d. Lista kodów klas odpowiedzi HTTP:
      100: kody informacyjne, 200: kody powodzenia, 300: kody przekierowań, 
      400: kody błędów klienta, 500: kody błedów serwera
   e. narzędia do testowania usług - postman/curl/soapui

4. Czym są wyrażenia regularne?
5. Jaka jest różnica pomiędzy deklaracją a inicjalizacją?
6. Czym jest rzutowanie typów?
7. Co to jest serializacja i deserializacja
   a. jajo serializ -des kura ///
   b. obj (ser) -      stream of byte -      db/file/memory        - stream of byte -    object

8. Czym jest object - instancja class
9. Aplikacja webowa - model MVC
10. Co oznacza ORM 
   SQLAlchemy to biblioteka do mapowania obiektowo-relacyjnego (ORM) dla języka Python/ C# EntityFramework

II. P Y T H O N

1. Struktury danych/zmienne
- Tuple - krotki niemutowalne immutable
  names = ('Jan', 'Anna', 'Tomek')
  W tupli dane można rozpakowywać:  a, b, c = names

- Lista jest mutowalna - oznacza, że dane można edytować.
  Możemy na przykład do listy dodawać nowe elementy:

  names.append('Adam') 
  names  # ['Jan', 'Anna', 'Tomek', 'Adam']

typy danych niemutowalne: int, float, decimal, complex, bool, string, tuple
var1="Ania"
var1.replace("a","o")
print(var1) -> Ania

2. Czy Python ma instrukcje switch?
  do wer 3.9 nie, jak ją zaimplemetować if/else, słownik def f(x): return {'a': 1, 'b': 2,}[x]
  
3. List comprehensions - to możliwość utworzenia nowej listy w oparciu, o listę już istniejąca
	Nowa lista, powinna zawierać tylko wartości parzyste:
	lista = [1,3,4,5,7,8]
	lista = [i for i in lista if i % 2 == 0 ]

	numbers = [x + 1 for x in range(5)]

1. Ternary operator 
   ret = 'even' if x % 2 == 0 else 'odd'

III. Relacyjne bazy danych:
Co oznacza NULL w SQL i jak stosować w klausuli WHERE?
Co to jest relacja wiele do wielu ? podaj przykład
Co to jest klucz obcy?
Co to jest trigger na bazie danych?
Jaka jest różnica między TRUNCATE a DELETE?
Co to jest indeks i jakie są jego rodzaje?
Co to jest transakcja?
Replikacja bazy danych.
Wyrażenia CTE?
SHOW DATATABLES/ SHOW TABLES/ USE DATABASE

Jaka jest kolejność wykonywania poleceń w SQL:
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
    1. FROM / JOIN /    2. WHERE/    3. GROUP BY     4. HAVING     
    5. SELECT   6. ORDER BY    7. LIMIT

Bazy nierelacyjne:
Czym są bazy danych NoSQL? (Redis, Elasticsearch)

IV. LINUX
Co to jest curl ?
W jaki sposób nadaje się lub usuwa uprawnienia do plików w Linux?
Co to jest cron w systemie Linux ?
Co to jest "grep" w systemie Linux i jak jego użyć? 
  grep wyraz plik
  history | grep fraza

Jak wyświetlić (edytować) plik w terminalu cat/less/vi?
Jak znaleźć plik ukryty ls -a?
System plików - struktura katalogów: /bin/dev/home/etc/lib/tmp/usr
Polecenia mv, scp, cp, ls, ll, wc, pwd, man
Monitorowanie zasobów i procesów: df - zajetość dysku, du - zajetość pliku, free - ram, ps - procesy, kill, top
Zapora sieciowa - iptables

HTML
Co to jest AJAX?
Atrybuty w strukturze html, przykład użycia id, class

