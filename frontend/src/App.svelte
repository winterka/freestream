<script>
  import { onMount, tick } from 'svelte';

  let photo;

  onMount(async () => {
    const res = await fetch('/api/get-tracks');
    const data = await res.json();
    await tick();
    console.log(data);
  });
</script>

<h1>Hello world</h1>
