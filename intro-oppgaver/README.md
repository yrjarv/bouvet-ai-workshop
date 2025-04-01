## 🚀 Kom i gang

### 1. Klon repoet

### 2. Sett opp miljøvariabler

For å kunne bruke Azure-tjenestene må vi legge til API-nøkler og endepunkter i en `.env`-fil. Dette bidrar til å holde sensitiv informasjon sikker.

_Slik gjør du:_

1. **Naviger til Backend-mappen**

Åpne en terminal og naviger til intro-oppgaver-mappen, deretter backend-mappen:

```bash
cd intro-oppgaver/backend
```

2. Opprett en `.env`-fil i rooten på backend-prosjektet.

3. Klikk på lenken under og kopier alt.
   - https://secret-service.bouvet.no/#/s/9b6c185d-b6e1-46ac-b8f6-e5f3b04b4664/xkxNIroVMWo3SBmVHplTWu
4. Lim inn i `.env`-filen

### 3. Kjør prosjektet

For å kjøre prosjektet anbefales det å bruke to separate terminaler: én for frontend og én for backend.

### Backend

Følg disse trinnene for å sette opp og kjøre backend:

1. **Naviger til Backend-mappen**  
   Åpne en terminal og naviger til intro-oppgaver-mappen, deretter backend-mappen:
   ```bash
   cd intro-oppgaver/backend
   ```
2. **Opprett et virtuelt miljø**
   ```bash
   python3 -m venv .venv
   ```
3. **Aktiver et virtuelt miljø**
   ```bash
   (Mac/linux) source .venv/bin/activate
   (Windows) .venv\Scripts\activate
   ```
4. **Installer nødvendige Python-pakker**
   ```bash
   pip3 install -r requirements.txt
   ```
5. **Kjør Flask server**

   ```bash
   flask run

   ```

*🚨 Første gang prosjektet kjøres, vil kommandoen "flask run" gi en feilmelding. Dette skyldes at det gjenstår noen oppgaver som må fullføres for at den skal fungere som forventet🚨*

### Frontend

Følg disse trinnene for å sette opp og kjøre frontend:

1. **Naviger til Frontend-mappen**
  Åpne en terminal og naviger til `frontend`-mappen:

   ```bash
   cd intro-oppgaver/frontend

   ```

2. **Installer avhengigheter**
   ```bash
   npm install
   ```
3. Run dev server
   ```bash
   npm run dev
   ```

## Oppgave 1 – OBJEKTGJENKJENNING 🔍

_I oppgave 1 skal vi bruke Azure Custom Vision for å gjenkjenne objekter (ingredienser) i et bilde. For å få til dette skal vi sette opp .env-fil, backend-route, og koble dette til frontend._

---

### 1.1 Opprett en route i Frontend for å vise hjemsiden

_Den ferdiglagde komponenten ImageUploadPage viser en side i frontenden der brukerne kan laste opp bilder. Vi skal nå sette opp en route som viser denne som hjemmesiden_

**Oppgave**

1. Naviger til `App.tsx`, som ligger i `src`-mappen.
2. Opprett en ny route med `path= "/"` som peker til komponenten **ImageUploadPage**.

Når du har fullført oppgaven, skal **ImageUploadPage** vises på skjermen.

### 1.2 Validering av filtype i SelectFileButton

_SelectFileButton-komponenten er en knapp som lar brukeren velge en fil (for eksempel et bilde) fra enheten sin._

**Oppgave**

1. Naviger til components/Buttons/SelectFileButton
2. Legg til en sjekk i knappen som sikrer at kun følgende filtyper aksepteres: .png, .jpg, .jpeg
   - Kontrollen skal også sørge for at filtypene er i små bokstaver (lowercase).

_Hint: Her kan man bruke accept-attributtet._

Når oppgaven er fullført, skal det kun være mulig å laste opp filer med formatene **.png**, **.jpg**, eller **.jpeg**.

### 1.3 Endre bakgrunnsfarge

1. Naviger til ` cd styles/index.css `
2. Nå er bakgrunnen hvit, endre den til favorittfargen din


### 1.4 Lag en knapp 

**Oppgave**

1.  **Naviger**:

    Naviger til `cd Buttons/UploadImageButton.tsx`

2.  **Last opp et bilde av kjøleskapet**:

    Last opp et bilde av et kjøleskap med ingredienser. Hvis du ikke har et slikt bilde, kan du også bruke et bilde fra internett.

3.  **Opprett en knapp**:

    Opprett en knapp med teksten "Send" og tilordne den CSS-klassen className={styles.buttons}.

4.  **Håndter knappens funksjonalitet**:

    Når brukeren klikker på knappen, skal bildet som er valgt lastes opp til API-et.  
     _Hint: Bruk `onClick`._

5.  **Sjekk om en fil er valgt**:

    Hvis ingen fil er valgt, logg meldingen "ingen fil er valgt" og returner en tom liste.



Når du har fullført oppgaven, skal det være mulig å klikke på knappen, og de identifiserte ingrediensene vil bli vist.

## Oppgave 2 – INNHOLDSGENERERING  🧠

_I oppgave 2 skal en oppskrift genereres basert på ingrediensene som ble valgt i forrige steg._

---



### 2.1 BILDEGENERERING 🖼️ 

Klassen `ImageGeneratorClient` er laget for å samhandle med OpenAI’s DALL-E 3-modell gjennom Azure OpenAI-tjenester, og brukes til å generere bilder basert på tekstbeskrivelser (kalt "prompt").

**Oppgave**

1. Naviger til `image_generator_client.py` i backend.

2. Sett modellen til **"dall-e-3"**.

3. Endre størrelsen på bilde til å være **1024x1024**.



### 2.2 TEKSTGENERERING 💬

Klassen LangueModelClient bruker OpenAI sin GPT-4-modell via Azure for å generere tekst basert på en prompt.
**Oppgave**

1. Naviger til `llm_client` i backend.

2. Sett modellen til **"gpt-4o-mini"**.


### 2.3 Forbedre Prompten 💡

_En godt formulert prompt er avgjørende for å generere relevante og presise resultater._

#### Oppgave

1. Gå gjennom eksisterende tekst i prompten i `recipe_generator.py`.

2. Sørg for at prompten er klar, spesifikk og inkluderer all nødvendig kontekst for å generere en oppskrift av høy
   kvalitet.



