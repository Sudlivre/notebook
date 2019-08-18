# Some problems with using react

## 2019-8-18

### The function used in render is undefined

Specify const to accept this.function in render, then use

### About the parent component passing values to the child component

**The subcomponent receives the last value**

using nextProps in component instead of this.props

```
componentWillReceiveProps(nextProps) {
  const {version} = nextProps;
}
```