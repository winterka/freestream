<script>
  import { onMount, tick } from 'svelte';

  let data = [];

  onMount(async () => {
    const res = await fetch('/api/get-tracks');
    data = await res.json();
    await tick();
    console.log(data);
  });
</script>

<main>
  <h2>text</h2>
  <div class="spread">
    {#each data as album}
      <figure>
        <img src={album[3]} alt={album[1]} />
        <figcaption>{album[1]}</figcaption>
      </figure>
    {:else}
      <!-- this block renders when photos.length === 0 -->
      <p>loading...</p>
    {/each}
  </div>
</main>

<style>
  .spread {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 8px;
  }

  figure,
  img {
    width: 100%;
    margin: 0;
  }
</style>
