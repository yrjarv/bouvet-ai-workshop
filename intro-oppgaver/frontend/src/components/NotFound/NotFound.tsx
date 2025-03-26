import styles from "./NotFound.module.css";

export function NotFound(props: { text: string }) {
  return (
    <div className={styles.notFoundContainer}>
      <img
        src="/sad_chef.jpg"
        alt="Sad Chef"
        className={styles.notFoundImage}
      />
      <p className={styles.notFoundText}>{props.text}</p>
    </div>
  );
}
