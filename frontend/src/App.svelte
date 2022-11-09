<script>
  import { onMount, tick } from 'svelte';
  import { isModalOpen } from './stores/modalStore.js';

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
  <div class="spread">
    {#each data as album}
      <Cover albumCoverUrl={album[3]} albumTitle={album[1]} />
    {/each}
  </div>

  {#if $isModalOpen}
    <div class="overlay" on:click={closeModal}>
      <Modal>
        <AudioPlayer src={data[0][2]} />
      </Modal>
    </div>
  {/if}
</main>

<style>
  main {
    color: #fff4e0;
  }

  h2 {
    text-align: center;
  }

  .spread {
    max-width: 70%;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
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
