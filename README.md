# Velkommen til Workshop med Bouvet!  
### Tema: Systemutvikling med integrering av Kunstig Intelligens  

I denne workshoppen skal vi utforske hvordan kunstig intelligens (AI) kan integreres i moderne systemutvikling. Gjennom praktiske oppgaver vil du bygge en applikasjon som kombinerer **React med TypeScript** i frontend og **Python** i backend.  

## 🌟 Hva skal vi lage?  
Applikasjonen vi jobber med, lar brukeren laste opp et bilde av et kjøleskap. Deretter vil  AI-modellen (custom vision):  
1. **Gjenkjenne objekter** i bildet og returnere en liste over matvarer.  
2. La brukeren redigere matvarelisten for å sikre nøyaktighet.  
3. Etter redigering vil:  
   - Open-AI-modellen (gpt-4o-mini) genererer en oppskrift basert på matvarene.  
   - Open-AI-modellen (dall-e-3) genererer et bilde av den ferdige retten!
4. Integrering med database i Azure 

Ved slutten av workshoppen vil du ha en fullverdig applikasjon som demonstrerer hvordan AI kan integreres i ulike steg av et system.  



## 🛠️ Teknologier vi bruker  
- **Frontend**: React med TypeScript  
- **Backend**: Python med relevante AI-biblioteker  
- **AI-modeller**: For bildebehandling (custom vision), oppskriftsgenerering (gpt-4o-mini) og bildeproduksjon (dall-e-3)
- **Database**: Azure data tables


## 🚀 Kom i gang  

### 1. Klon repoet  

### Backend  

Follow these steps to set up and run the backend:  

1. **Navigate to the Backend Folder**  
   Open a terminal and navigate to the `backend` directory:  
   ```bash  
   cd backend  
2. **Create a virtual enviroment**
    ```bash
    python3 -m venv .venv
3. **Activate the virtual enviroment**
    ```bash
    (Mac/linux) source .venv/bin/activate 
    (Windows) .venv\Scripts\activate
4. **Install neccessary Python packages**
    ```bash
    pip3 install -r requirements.txt
5. **Run Flask server**
    ```bash
    flask run
    
### Frontend
Follow these steps to set up and run the frontend:
1. **Navigate to the Frontend Folder**
   Open a terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend

2. **Install dependencies**
    ```bash
   npm install
3. Run dev server
    ```bash
   npm run dev
