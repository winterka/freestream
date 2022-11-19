<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { isModalOpen, modalContent } from './stores/modalStore.js';

  import Cover from './lib/Cover.svelte';
  import Modal from './lib/Modal.svelte';
  import AudioPlayer from './lib/AudioPlayer.svelte';

  let data: any[] = [];

  onMount(async () => {
    const res: Response = await fetch('/api/get-tracks');
    data = await res.json();
    await tick();
    console.log(data);
  });
</script>

<main>
  <h2>Test</h2>
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
    <Modal>
      <AudioPlayer src={$modalContent} />
    </Modal>
  {/if}
</main>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  h2 {
    text-align: center;
    margin-top: 15px;
  }

  ul {
    list-style: none;
  }

  .container {
    padding: 17px 5%;
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
</style>
