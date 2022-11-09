<script>
  export let albumCoverUrl;
  export let albumTitle;

  import { isModalOpen } from '../stores/modalStore.js';
  import { modalContent } from '../stores/modalStore.js';

  function openModal() {
    $isModalOpen = true;
    $modalContent = albumTitle;
  }
</script>

<figure on:click={openModal}>
  <img src={albumCoverUrl} alt={albumTitle} width="150" />
  <figcaption>{albumTitle}</figcaption>
</figure>

<style>
  figure,
  img {
    display: block;
    margin: 0;
    width: 100%;
    cursor: pointer;
  }

  figcaption {
    text-align: center;
    margin-top: 0.2rem;
    font-size: 1.1rem;
  }
</style>
