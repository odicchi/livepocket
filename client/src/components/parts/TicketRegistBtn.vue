<template>
  <button
    :class="classes"
    :disabled="disabled"
    type="button"
    @click="registClick"
  >
    <slot />
  </button>
</template>

<script>
export default {
  name: 'TicketRegistBtn',

  props: {
    type: {
      type: String,
      default: 'button'
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },

  computed: {
    // `type`に応じてクラスを動的に生成する
    classes () {
      const cls = this.type === 'text' ? ('-' + this.type) : ''
      return [`kbn-button${cls}`]
    }
  },

  methods: {
    // `click`イベントを発行
    registClick (ev) {
      this.$emit('click', ev)
    }
  }
}
</script>

<style scoped>
.kbn-button {
  padding: .6em, 1.3em;
}

.kbn-button-text {
  border: none;
  padding-right: 0;
  padding-left: 0;
}
</style>