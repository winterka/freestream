<script lang="ts">
  import { isModalOpen } from '../stores/modalStore.js';

  function openModal(): void {
    $isModalOpen = true;
  }

  function closeModal(): void {
    $isModalOpen = false;
  }
</script>

<div class="outer-modal" on:click={closeModal}>
  <div class="inner-modal" on:click|stopPropagation={openModal}>
    <slot />
    <button on:click={closeModal}>&times;</button>
  </div>
</div>

<style>
  .outer-modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.55);
    /* backdrop-filter: blur; */
    overflow: auto;
  }

  .inner-modal {
    background-color: rgba(44, 44, 44, 0.85);
    margin: 15% auto;
    padding: 20px;
    width: 30%;
    overflow: auto;
  }

  button {
    /* position: relative;
      top: 0.5rem;
      right: 1rem;
      font-size: 1.7rem;
      color: rgb(255, 244, 224);
      cursor: pointer;
      border: none;
      background: none; */

    color: rgb(255, 244, 224);
    float: right;
    border: none;
    background: none;
    font-size: 24px;
  }

  button:hover {
    color: rgb(255, 59, 59);
    cursor: pointer;
  }

  button:active {
    color: rgb(173, 0, 0);
  }
</style>
