# Analiza danych w czasie rzeczywistym - Lab2

## Aplikacja API zbudowana w ramach zadania laboratoryjnego

### Jak uruchomić:

1. Zainstaluj wymagane biblioteki:
   pip install -r requirements.txt

2. Uruchom aplikację:
   python app.py

3. Przetestuj aplikację:
   python test_app.py

### Endpointy:

- `/` – strona domowa
- `/mojastrona` – strona informacyjna
- `/hello?name=TwojeImie` - strona z przywitaniem użytkownika
- `/api/v1.0/predict?num1=3&num2=4` – zwraca predykcję
