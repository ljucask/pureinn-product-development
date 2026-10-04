window.HARNESS_CONFIG = {
  name: 'fixture', title: 'Fixture',
  screens: [
    { label: 'Queue', src: 'index.html', desc: 'The queue.', feature: 'PRT-T-001' },
    { label: 'Settings', src: 'settings.html', desc: 'Admin settings.', feature: 'PRT-T-005' },
    { label: 'Feature map', featureMap: true, icon: 'board', desc: 'Plan.' },
    { label: 'What is real', disclosure: true, icon: 'info', desc: 'Disclosure.' }
  ],
  states: ['empty', 'full', 'error', 'unauth'],
  variants: [],
  roles: [ { id: 'dispatcher', label: 'Dispatcher', desc: 'Runs the queue.' }, { id: 'admin', label: 'Admin' } ],
  phases: [ { id: 'mvp', label: 'MVP' }, { id: 'p1', label: 'Phase 1' }, { id: 'p2', label: 'Phase 2' } ],
  versions: [ { id: 'header', label: 'Header', options: ['A', 'B'] } ],
  view: { phase: 'mvp' },
  features: [
    { id: 'PRT-T-001', name: 'Queue', phase: 'mvp', status: 'built', desc: 'The list of jobs.', spec: 'Said in review: order by deadline.', card: 'cards/PRT-T-001.md' },
    { id: 'PRT-T-002', name: 'Bulk assign', phase: 'p1', status: 'built' },
    { id: 'PRT-T-003', name: 'Map', phase: 'p2', on: { 'index.html': ['#map', '::bad(('] } },
    { id: 'PRT-T-004', name: 'Audit', phase: 'mvp', roles: ['admin'] },
    { id: 'PRT-T-005', name: 'Settings', phase: 'p1', roles: ['admin'], on: { '*': ['a[href="settings.html"]'] } }
  ],
  annotations: {},
  disclosure: { proves: 'a', doesNotProve: 'b', classification: 'Reference' },
  review: { task: 'Try it.' }
};
