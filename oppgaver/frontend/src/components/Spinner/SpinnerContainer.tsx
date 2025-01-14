import styles from "./SpinnerContainer.module.css";

interface Props {
  message: string;
}

export function SpinnerContainer({ message }: Props) {
  return (
    <div className={styles.spinnerOverlay}>
      <div className={styles.spinnerBox}>
        <div className={styles.text}>{message}</div>
        <div className={styles.spinnerContainer}>
          <div className={styles.spinner}></div>
        </div>
      </div>
    </div>
  );
}
