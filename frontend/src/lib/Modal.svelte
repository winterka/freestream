<script>
  import { isModalOpen } from '../stores/modalStore.js';
  // import { modalContent } from '../stores/modalStore.js';

  function openModal() {
    $isModalOpen = true;
  }

  function closeModal() {
    $isModalOpen = false;
  }
</script>

<div on:click|stopPropagation={openModal}>
  <slot />
  <button on:click={closeModal}>x</button>
</div>

<style>
  div {
    color: #1a1a1d;
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 20%;
    height: 50%;

    background-color: rgba(44, 44, 44, 0.85);
    padding: 6rem;
    border-radius: 5px;
    /* box-shadow: 0 3rem 5rem rgba(0, 0, 0, 0.3); */
    z-index: 10;
  }

  button {
    position: absolute;
    top: 0.5rem;
    right: 1rem;
    font-size: 1.7rem;
    color: rgb(255, 244, 224);
    cursor: pointer;
    border: none;
    background: none;
  }

  button:hover {
    color: rgb(255, 59, 59);
  }

  button:active {
    color: rgb(173, 0, 0);
  }
</style>
