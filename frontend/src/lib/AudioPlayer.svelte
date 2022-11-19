<script lang="ts">
  export let src: string;

  let audio: any;
  let paused: boolean = true;
</script>

<audio bind:this={audio} bind:paused controls {src} />
