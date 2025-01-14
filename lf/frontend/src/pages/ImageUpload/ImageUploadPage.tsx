import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import UploadIcon from "../../images/UploadIcon.tsx";
import styles from "./ImageUpload.module.css";
import IngredientTagsContainer from "../../components/IngredientTagsContainer/IngredientTagsContainer.tsx";
import RecipesContext from "../../context/RecipesContext.tsx";
import { SpinnerContainer } from "../../components/spinner/SpinnerContainer.tsx";
import { SelectFileButton } from "../../components/buttons/SelectFileButton.tsx";
import UploadImageButton from "../../components/buttons/UploadImageButton.tsx";

export function ImageUploadPage() {
  type UploadState = "ERROR" | "IDLE" | "LOADING" | "WAITING_FOR_TAGS";

  const [file, setFile] = useState<File | null>(null);
  const [tags, setTags] = useState<string[]>([]);
  const [state, setState] = useState<UploadState>("IDLE");
  const { recipeList, setRecipes } = useContext(RecipesContext);

  const navigate = useNavigate();

  function handleFileChange(selectedFile: File | null) {
    setFile(selectedFile);
    setState("IDLE");
  }

  function getPageContent() {
    if (state === "LOADING") {
      return (
        <SpinnerContainer message="Laster" />
      );
    }

    if (state == "ERROR") {
      return (
        <>
          <img
            src="/sad_chef.jpg"
            alt="Sad Chef"
            className={styles.errorImage}
          />
          <p style={{ color: "red" }}>
            Noe gikk galt. Vennligst prøv igjen.
          </p>
          <button onClick={() => setState("IDLE")}>Start på nytt</button>
        </>
      );
    }

    if (state == "IDLE") {
      return (
        <>
          <div className={styles.containerSmaller}>
            <div className={styles.icon}>
              <UploadIcon />
            </div>
            <div className={styles.rowContainer}>
              <div className={styles.text}>Dra og slipp eller</div>
              <SelectFileButton onFileChange={handleFileChange} />
            </div>
            {file && (
              <div className={styles.fileInfo}>
                <span>Opplastet fil: {file.name}</span>
              </div>
            )}
            {file && (
              <UploadImageButton
                file={file}
                onSend={() => setState("LOADING")}
                onDone={(tags) => {
                  if (tags) {
                    setTags(tags);
                    setState("WAITING_FOR_TAGS");
                  } else {
                    setState("ERROR");
                  }
                }}
              />
            )}
            {!file && (
              <div className={styles.textSmall}>
                Aksepterte filtyper er png, jpg, jpeg, svg
              </div>
            )}
          </div>
        </>
      );
    }
  }

  if (state == "WAITING_FOR_TAGS") {
    return (
      <div className={styles.containerSmaller}>
        <IngredientTagsContainer
          aiTags={tags}
          setLoading={() => setState("LOADING")}
          onDone={(recipe) => {
            if (recipe) {
              setRecipes([...(recipeList || []), recipe]);
              navigate("/recipes/" + recipe.id);
            } else {
              setState("ERROR");
            }
          }}
        />
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.uploadBox}>
        {getPageContent()}
      </div>
    </div>
  );
}
