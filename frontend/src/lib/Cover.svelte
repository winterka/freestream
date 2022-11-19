<script lang="ts">
  export let albumCoverUrl: string;
  export let albumTitle: string;
  export let albumTrack: string;

  import { isModalOpen, modalContent, dummyFn } from '../stores/modalStore';

  function openModal(): void {
    $isModalOpen = true;
    $modalContent = albumTrack;
  }
</script>

<li on:click={openModal} on:keydown={dummyFn}>
  <img src={albumCoverUrl} alt={albumTitle} />
  <div class="overlay"><h3>{albumTitle}</h3></div>
</li>

<style>
  li {
    flex-basis: 250px;
    position: relative;
    cursor: pointer;
  }

  li img {
    object-fit: cover;
    max-width: 100%;
    height: auto;
    vertical-align: middle;
    border-radius: 5px;
  }

  .overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(57, 57, 57, 0.5);
    top: 0;
    left: 0;
    opacity: 0;
    transition: opacity 0.2s;
    border-radius: 5px;

    display: flex;
    align-items: center;
    justify-content: center;
  }

  li:hover .overlay {
    opacity: 1;
  }
</style>
