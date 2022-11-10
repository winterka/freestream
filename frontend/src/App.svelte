<script>
  import { onMount, tick } from 'svelte';
  import { isModalOpen, modalContent } from './stores/modalStore.js';

  import Cover from './lib/Cover.svelte';
  import Modal from './lib/Modal.svelte';
  import AudioPlayer from './lib/AudioPlayer.svelte';

  let data = [];

  onMount(async () => {
    const res = await fetch('/api/get-tracks');
    data = await res.json();
    await tick();
    console.log(data);
  });

  function closeModal() {
    $isModalOpen = false;
  }
</script>

<main>
  <h2>text</h2>
  <div class="container">
    <ul class="cover-gallery">
      {#each data as album (album[0])}
        <Cover
          albumCoverUrl={album[3]}
          albumTitle={album[1]}
          albumTrack={album[2]}
        />
      {/each}
    </ul>
  </div>

  {#if $isModalOpen}
    <div class="overlay" on:click={closeModal}>
      <Modal>
        <AudioPlayer src={$modalContent} />
      </Modal>
    </div>
  {/if}
</main>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  main {
    color: #fff4e0;
  }

  h2 {
    text-align: center;
  }

  ul {
    list-style: none;
  }

  .container {
    padding: 20px 5%;
  }

  .cover-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }

  .cover-gallery::after {
    content: '';
    flex-basis: 250px;
  }

  .overlay {
    position: fixed;
    padding: 0;
    margin: 0;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    background-color: rgba(0, 0, 0, 0.55);
    backdrop-filter: blur;
  }
</style>
