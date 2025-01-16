## Oppgave 1 – OBJECT RECOGNITION

_Azure Custom Vision blir brukt for å gjenkjenne objekter (ingredienser) i et bilde. For å få til dette skal vi sette opp .env-fil, backend-route, og koble tdette til frontend._

---

### 1.1 Oppsett av miljøvariabler

For å kunne bruke Azure-tjenestene må vi legge til API-nøkler og endepunkter i en `.env`-fil. Dette bidrar til å holde sensitiv informasjon sikker.

**Oppgave**


1. Opprett en `.env`-fil i rooten av prosjektet.
2. Legg til følgende variabler i `.env`-filen:

```
AZURE_ENDPOINT="https://dummy_endpoint.cognitiveservices.azure.com/"
AZURE_API_KEY="dummy_api_key_goes_here"
```

### 1.2 Opprett en route i Frontend for å vise hjemsiden

_Vi trenger en side i frontenden der brukerne kan laste opp bilder._

**Oppgave**

1. Naviger til app.tsx
2. Opprett en ny route som peker til den ferdiglagde komponenten ImageUploadPage.

### 1.3 Validering av filtype i SelectFileButton

_SelectFileButton-komponenten er en knapp som lar brukeren velge en fil (for eksempel et bilde) fra enheten sin._

**Oppgave**

1. Legg til en sjekk i knappen som sikrer at kun følgende filtyper aksepteres: .png, .jpg, .jpeg, .svg

_Hint: Her kan man bruke accept-attributtet._

### 1.4 Backend-route for å gjenkjenne ingredienser

_Når en `POST`-forespørsel sendes til `/recognize_ingredients`, skal bildet som er sendt med forespørselen behandles av Azure Custom Vision for å gjenkjenne ingredienser. Forespørselen skal inneholde et bilde, og endepunktet skal returnere ingrediensene som ble gjenkjent._

**Oppgave**

1.  Lag et nytt endepunkt i `routes.py` som tar imot bildet.
2.  Finn ut hvilken klasse som må brukes for å kalle Custom Vision i Azure.
3.  Returner en JSON-formatert liste med ingredienser, for eksempel:

```json
["paprika", "onion", "fish oil"]
```

### 1.5 Frontend – Fetch-kall

_I denne oppgaven skal du gjøre endringer i UploadImageButton.tsx som ligger i button-komponenten. Komponenten er designet for at brukeren skal kunne laste opp et bilde til et API for å identifisere ingredienser. Når opplastingen er fullført, skal resultatene fra API-et vises som en liste._

**Oppgave**

1.  **Opprett en knapp**:  
     Opprett en knapp med teksten "Send" og tilordne den CSS-klassen className={styles.buttons}.
2.  **Håndter knappens funksjonalitet**:
    Når brukeren klikker på knappen, skal bildet som er valgt lastes opp til API-et.  
     _Hint: Bruk `onClick`._
3.  **Sjekk om en fil er valgt**:
    Hvis ingen fil er valgt, logg meldingen "ingen fil er valgt" og returner en tom liste.

4.  **Lag API-kall**:  
     Bruk et POST-kall til følgende URL:  
     `http://127.0.0.1:5000/recognize_ingredients`.  
     Bildet skal sendes som FormData med nøkkelen `"image"`.

5.  **Konverter responsen til JSON-format**:
    Konverter responsen fra serveren til å være JSON-format

## Oppgave 2 – CONTENT GENERATION

_I oppgave 2 skal en oppskrift genereres basert på ingrediensene som ble valgt i forrige steg._

---

### 2.1 Kall generate_recipe fra frontenden

_I IngredientTagsContainer.tsx finnes det en funskjon `generateRecipe`, som skal kalles når man ønsker å sende listen med tags til backend, og generere en oppskrift. Denne funksjonen er ikke ferdig implementert_

**Oppgave**

1. Fullfør implementasjonen av `generateRecipe`. Den skal ta imot en liste av tags (`tags: string[]`), og sende disse til `/generate_recipe` endpointet.
2. Hvis responsen er OK, konverter resultatet fra backend til JSON med `await response.json()`.
3. Bruk oppskriften (JSON-data) fra responsen og kall `onDone`-funksjonen med oppskriften.

### 2.2 Implementer RecipeGenerator

_I backend finnes det en klasse `RecipeGenerator` som er ansvarlig for å generere en oppskrift basert på en liste med
ingredienser. Foreløpig returnerer denne klassen bare dummy-data._

#### Oppgave

Gjør klassen `RecipeGenerator` i stand til å:

1. Ta imot en liste med ingredienser som input.
2. Kalle alle nødvendige Azure-tjenester for å generere en oppskrift.
3. Returnere en komplett og strukturert oppskrift som resultat.

### 2.3 Forbedre Prompten

_En godt formulert prompt er avgjørende for å generere relevante og presise resultater._

#### Oppgave

- Gå gjennom eksisterende tekst i prompten i `recipe_generator.py`.
- Sørg for at prompten er klar, spesifikk og inkluderer all nødvendig kontekst for å generere en oppskrift av høy
  kvalitet.

## Oppgave 3 – DATABASEOPPGAVEN (Azure Table Service)

_Nå skal vi lagre den genererte oppskriften i en database, og hente ut tidligere genererte oppskrifter og vise disse i
frontend. Vi bruker Azure Table Service (en enkel NoSQL-løsning) for å
gjøre dette._

---

### 3.1 Lagring av resultatet

### Oppgave

Etter `generate_recipe` er ferdig med å generere en oppskrift,
Når generate_recipe kjører, bruk save_recipe for å sende dataene til databasen. Denne funksjonen tar to argumenter.
Først, oppskriften, som vi allerede har, og nummer to, en unik bruker-id `user_id`. Finn funksjonen `useUserId()` i
frontend, og bruk denne til å sende med `user_id` i `generate_recipe` requesten.

### 3.3 Hent ut oppskrifter – get_recipes

Om Forrige steg er gjort riktig, skal
oppskriftene dine ligge i Azure Table Service, og det er nå mulig å skrive en funskjon for å hente ut alle oppskrifter
som tilhører deg, og vise disse i frontend.

### Oppgave

I database.py finnes det en funksjon `get_recipes`. Denne er delvis implementert, og gjør følgende:

- lager en query som spør etter alle oppskrifter som matcher din `user_id`
- kaller Azure klienten for å hente ut dataen

For å fullføre funksjonen, må du iterere over dataene, og returnere en liste over oppskrifter.
