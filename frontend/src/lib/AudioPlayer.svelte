<script>
  export let src;

  let audio;
  let paused = true;
</script>

<audio bind:this={audio} bind:paused controls {src} />
