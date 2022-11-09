<script>
  import { onMount, tick } from 'svelte';

  let json;

  onMount(async () => {
    const res = await fetch('/api/get-tracks');
    json = await res.json();
    await tick();
    console.log(json);
  });
</script>

<p>{json}</p>
