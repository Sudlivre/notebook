# Some problems with using react

## 2019-8-18

### The function used in render is undefined

Specify const to accept this.function in render, then use

### About the parent component passing values to the child component

**The subcomponent receives the last value**

using nextProps in component instead of this.props

```javascript
componentWillReceiveProps(nextProps) {
  const {version} = nextProps;
}
```

### Add component for Ant Design Pro
```shell
npx umi block add DashboardAnalysis --path=dashboard/analysis --js --npm-client cnpm
npx umi block add DashboardMonitor --path=dashboard/monitor --js --npm-client cnpm
npx umi block add DashboardWorkplace --path=dashboard/workplace --js --npm-client cnpm
npx umi block add FormBasicForm --path=form/basic-form --js --npm-client cnpm
npx umi block add FormStepForm --path=form/step-form --js --npm-client cnpm
npx umi block add FormAdvancedForm --path=form/advanced-form --js --npm-client cnpm
npx umi block add ListSearchArticles --path=list/search/articles --js --npm-client cnpm
npx umi block add ListSearchProjects --path=list/search/projects --js --npm-client cnpm
npx umi block add ListSearchApplications --path=list/search/applications --js --npm-client cnpm
npx umi block add ListTableList --path=list/table-list --js --npm-client cnpm
npx umi block add ListBasicList --path=list/basic-list --js --npm-client cnpm
npx umi block add ListCardList --path=list/card-list --js --npm-client cnpm
npx umi block add ProfileBasic --path=profile/basic --js --npm-client cnpm
npx umi block add ProfileAdvanced --path=profile/advanced --js --npm-client cnpm
npx umi block add ResultSuccess --path=result/success --js --npm-client cnpm
npx umi block add ResultFail --path=result/fail --js --npm-client cnpm
npx umi block add Exception403 --path=exception/403 --js --npm-client cnpm
npx umi block add Exception404 --path=exception/404 --js --npm-client cnpm
npx umi block add Exception500 --path=exception/500 --js --npm-client cnpm
npx umi block add AccountCenter --path=account/center --js --npm-client cnpm
npx umi block add AccountSettings --path=account/settings --js --npm-client cnpm
npx umi block add EditorFlow --path=editor/flow --js --npm-client cnpm
npx umi block add EditorMind --path=editor/mind --js --npm-client cnpm
npx umi block add EditorKoni --path=editor/koni --js --npm-client cnpm
```